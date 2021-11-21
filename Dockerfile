FROM python:3.8.0
ENV PYTHONUNBUFFERED 1

RUN mkdir /todoproject
WORKDIR /todoproject

# COPY . .


COPY ./static ./static
COPY ./templates ./templates
COPY ./todoapp ./todoapp
COPY ./todolist ./todolist
COPY ./manage.py .
COPY ./db.sqlite3 .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]
