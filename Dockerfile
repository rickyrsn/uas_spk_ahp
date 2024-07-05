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

# Expose port yang akan digunakan oleh Flask
EXPOSE 5000

# Perintah untuk menjalankan aplikasi
CMD ["flask", "run", "--host=0.0.0.0"]
