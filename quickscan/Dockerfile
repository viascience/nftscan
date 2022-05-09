FROM ubuntu

# Install quickscan
RUN apt update

RUN apt install python3 python3-pip -y

# Flask install
RUN pip install flask

COPY ./app_files /app_files
WORKDIR /app_files

ENV FLASK_APP=/app_files/routes.py

CMD ["flask", "run", "-h", "0.0.0.0", "--port=5001"]
