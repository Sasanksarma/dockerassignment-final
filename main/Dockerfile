FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install mysql-connector

EXPOSE 8021

CMD ["python", "app.py"]
