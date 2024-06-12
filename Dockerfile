FROM python:3.9

WORKDIR . /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# 2. Скопируйте код приложения
COPY . .

CMD ["python", "main.py"]