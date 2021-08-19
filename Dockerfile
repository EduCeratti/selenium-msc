FROM alpine

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" > /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories

RUN apk update
RUN apk add chromium
RUN apk add chromium-chromedriver

RUN apk add python3
RUN python3 -m ensurepip
RUN pip3 install -U selenium

WORKDIR /app

COPY msisdn_list.txt /app/
COPY run.sh /app/
COPY msc.py /app/

# RUN sh /app/run.sh
