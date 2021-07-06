FROM python:3.6.9-slim-buster as base
WORKDIR /app
RUN apt-get update -qq && \
    apt-get install -yqq apt-utils && \
    apt-get install -yqq procps && \
    apt-get install -yqq gcc &&\
    apt-get install -yqq --no-install-recommends vim && \
    apt-get install -yqq make && \
    apt-get install -yqq git && \
    apt-get clean
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy
ADD . . 
