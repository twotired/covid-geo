FROM docker.io/library/alpine:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN adduser -D -h /home/django -s /bin/sh django

WORKDIR /code
COPY requirements.txt /code

RUN apk update && \
  apk add --no-cache \
          gcc \
          gdal \
          htop \
          lsof \
          musl-dev \
          postgresql-client \
          postgresql-dev \
          py3-pip \
          python3-dev \
          py3-setuptools \
          python3 \
          vim && \
  pip3 install -qq --no-cache-dir --upgrade pip && \
  pip3 install -qq --no-cache-dir --ignore-installed six -r requirements.txt && \
  apk del \
          gcc \
          musl-dev \
          openssl-dev \
          postgresql-dev \
          python3-dev \
          py3-setuptools

#RUN ln /usr/bin/python3 /usr/bin/python

CMD python3

USER django
