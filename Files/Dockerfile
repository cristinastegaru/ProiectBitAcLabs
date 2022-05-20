FROM python:3.10-bullseye

RUN mkdir /app
ADD . /app
WORKDIR /app

ENV TZ=Europe/Bucharest

RUN pip install -r Files/requirements.txt

CMD python /app/Files/main.py