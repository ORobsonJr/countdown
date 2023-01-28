FROM python:latest
COPY . /app
RUN pip install django
WORKDIR /app
CMD python manage.py runserver

