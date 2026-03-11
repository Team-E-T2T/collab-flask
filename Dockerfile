FROM python:3.12-alpine

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy application
COPY . .

# Cloud Run listens on port 8080
ENV PORT=8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]