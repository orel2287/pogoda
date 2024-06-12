FROM python:3.9

WORKDIR /app

RUN pip install Flask requests

COPY . /app

CMD ["python", "main.py"]
