FROM ubuntu

# Install stegseek
RUN apt update
RUN apt install wget -y
RUN wget https://github.com/RickdeJager/stegseek/releases/download/v0.6/stegseek_0.6-1.deb
RUN apt install ./stegseek_0.6-1.deb -y

RUN apt install python3 python3-pip -y

# Flask install
RUN pip install flask

COPY ./app_files /app_files
COPY ./rockyou.txt /app_files
WORKDIR /app_files

ENV FLASK_APP=/app_files/routes.py

CMD ["flask", "run", "-h", "0.0.0.0", "--port=5001"]
