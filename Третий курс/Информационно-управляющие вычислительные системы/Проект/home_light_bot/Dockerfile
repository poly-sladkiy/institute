FROM python:3.10.4-slim

RUN mkdir /bot

COPY . /bot
RUN pip install -r /bot/requirements.txt

CMD python3 /bot/app.py
