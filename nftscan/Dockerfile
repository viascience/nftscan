FROM alpine

# Flask install
RUN apk add --no-cache python3 py3-pip
RUN pip install flask pyyaml configparser
RUN mkdir app

COPY ./app_files /app_files
COPY docker-compose.yml /app_files/docker-compose.yml
WORKDIR /app_files

ENV FLASK_APP=/app_files/routes.py

CMD ["flask", "run", "-h", "0.0.0.0"]
