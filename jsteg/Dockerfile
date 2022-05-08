FROM alpine

# Install jsteg
RUN wget -O /usr/bin/jsteg https://github.com/lukechampine/jsteg/releases/download/v0.1.0/jsteg-linux-amd64
RUN chmod +x /usr/bin/jsteg
RUN wget -O /usr/bin/slink https://github.com/lukechampine/jsteg/releases/download/v0.2.0/slink-linux-amd64
RUN chmod +x /usr/bin/slink
RUN mkdir /data


# Flask install
RUN apk add --no-cache python3 py3-pip
RUN pip install flask
RUN mkdir app

COPY ./app_files /app_files
WORKDIR /app_files

ENV FLASK_APP=/app_files/routes.py

CMD ["flask", "run", "-h", "0.0.0.0"]

