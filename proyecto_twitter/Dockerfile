FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY  . ./

CMD python3 ./test_twitter.py; python3 ./Twitter.py
