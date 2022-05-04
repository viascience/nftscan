FROM alpine

# Install jsteg
RUN wget -O /usr/bin/jsteg https://github.com/lukechampine/jsteg/releases/download/v0.1.0/jsteg-linux-amd64
RUN chmod +x /usr/bin/jsteg
RUN wget -O /usr/bin/slink https://github.com/lukechampine/jsteg/releases/download/v0.2.0/slink-linux-amd64
RUN chmod +x /usr/bin/slink
RUN mkdir /data

RUN apk add --no-cache python3 py3-pip
RUN pip install flask
RUN mkdir app

#ENV FLASK_APP

#RUN flask run

