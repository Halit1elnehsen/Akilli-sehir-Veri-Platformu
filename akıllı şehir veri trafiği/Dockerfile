FROM python:3.11-slim

WORKDIR /app

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Scriptleri kopyala
COPY veri_yukleyici.py .
COPY enerji_gorsellestirme.py .

# Varsayılan olarak veri yükleyiciyi çalıştır (unbuffered)
CMD ["python", "-u", "veri_yukleyici.py"]
