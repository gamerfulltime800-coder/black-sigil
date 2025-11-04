FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY black_sigil_bot.py .

CMD ["python", "black_sigil_bot.py"]
