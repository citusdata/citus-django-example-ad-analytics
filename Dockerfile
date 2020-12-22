FROM debian:buster-slim

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    make \
    openssl \
    pipenv \
    python3 \
    python3-setuptools \
    python3-wheel \
    python3-psycopg2 \
    python3-gevent \
    python3-psutil \
    python3-dev \
    libev-dev \
    libev-libevent-dev \
    postgresql-client-11 \
    net-tools \
    lsof \
    curl \
    sudo \
  && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /usr/src/citus-django-example-ad-analytics

# avoid re-installing Python dependencies when Makefile has changed
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY Makefile ./
COPY manage.py ./
COPY benchmarkresult/ ./benchmarkresult/
COPY ./scripts/ ./scripts/
COPY ./src/ ./src/
