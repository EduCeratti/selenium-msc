FROM alpine

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" > /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories

RUN apk update
RUN apk add chromium
RUN apk add chromium-chromedriver

COPY requirements.txt /app/

RUN apk add python3
RUN python3 -m ensurepip
#RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

WORKDIR /app

COPY msisdn_list.txt /app/

copy msc_execution.log /app/
COPY run.sh /app/
COPY msc.py /app/
COPY api.py /app/
COPY run_api.sh /app/

RUN ["chmod", "+x", "/app/run.sh"]

EXPOSE 4447

CMD ["python3", "/app/api.py"]
