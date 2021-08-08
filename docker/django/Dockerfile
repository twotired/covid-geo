FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN apt-get upgrade
RUN apt-get update
RUN apt-get install -y gdal-bin postgresql-client-11 vim

WORKDIR /code

COPY requirements.txt /code
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD python3

RUN adduser django

USER django
