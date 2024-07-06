# Gunakan image Python sebagai base image
FROM python:3.9-slim

# Tentukan working directory di dalam container
WORKDIR /app

# Copy requirements file ke working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh isi proyek ke working directory
COPY . .

# Set environment variable untuk Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# RUN flask db init || true && flask db migrate -m 'Initial migration' || true && flask db upgrade || true

# Expose port yang akan digunakan oleh Flask
EXPOSE 5000

# Perintah untuk menjalankan aplikasi
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:5000 --workers 3 app:app"]
