FROM ubuntu:16.04

MAINTAINER Pierre <pierre.dahlstrom@vaimo.com>

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev libmysqlclient-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY app.py /app

ENTRYPOINT [ "flask" ]

CMD [ "run", "--host", "0.0.0.0" ]