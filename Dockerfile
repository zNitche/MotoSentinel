FROM python:3.9-buster

COPY . /MotoSentinel
WORKDIR /MotoSentinel

RUN apt update
RUN apt -y install nano python3-setuptools python3-dev python3-rpi.gpio python3-matplotlib

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt -v

CMD python3 app.py