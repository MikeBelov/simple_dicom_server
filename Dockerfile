FROM python:3.8-slim
WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r

COPY . .

EXPOSE 11112
CMD python server.py

