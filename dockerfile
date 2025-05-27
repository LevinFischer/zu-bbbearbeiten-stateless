# Verwende ein offizielles Python-Image als Basis
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Dateien ins Image kopieren
COPY . .

# Abhängigkeiten installieren
RUN pip install --no-cache-dir flask

# Expose Flask-Port (z. B. 5000)
EXPOSE 5000

# Startbefehl
CMD ["python", "main.py"]

LABEL org.opencontainers.image.source=https://github.com/levinfischer/zu-bbbearbeiten-stateless