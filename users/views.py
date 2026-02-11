from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, ProfileRegisterForm, LoginForm, ProfileUpdateForm
from .models import Profile

# Create your views here.
class RegisterView(CreateView):
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    form_class = UserRegisterForm

    # def form_valid(self, form):
    #     user = form.save()
    #     user.groups.add(Group.objects.get(name="user"))
    #     login(self.request, user)
    #     return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("profile")

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")

class UsersListView(LoginRequiredMixin,  ListView):
    model = Profile
    template_name = "users/users_list.html"


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "users/profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return self.request.user.profile

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "users/profile_edit.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user


