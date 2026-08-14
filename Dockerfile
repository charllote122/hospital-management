FROM python:3.11.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=hospital_api.settings

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    libpng-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Run migrations and collect static
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput --clear

# Expose port
EXPOSE 8000

# Start gunicorn
CMD ["gunicorn", "hospital_api.wsgi:application", "--workers=2", "--bind=0.0.0.0:8000"]
