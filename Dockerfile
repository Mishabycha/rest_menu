FROM python:3.12-slim
# щоб не створювався .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# щоб логи одразу виводились
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt 

COPY . /app/

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

ENTRYPOINT [ "gunicorn", "REST_MENU.wsgi", "-b", "0.0.0.0:8000" ]