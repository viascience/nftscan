FROM ubuntu

# Install stegseek
RUN apt update
RUN apt install wget -y
RUN wget https://github.com/RickdeJager/stegseek/releases/download/v0.6/stegseek_0.6-1.deb
RUN apt install ./stegseek_0.6-1.deb -y


# Install API
RUN apt install python3 python3-pip -y
RUN mkdir data

RUN pip install flask

#ENV FLASK_APP=

#RUN flask run
