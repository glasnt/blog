FROM python:3.8-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apt-get update && apt-get install wkhtmltopdf -y

COPY . ./

RUN pip install -r requirements.txt 


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
