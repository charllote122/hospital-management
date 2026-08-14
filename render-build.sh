#!/bin/bash
echo "🐍 Python version: $(python --version)"

# Install system dependencies
echo "📦 Installing system dependencies..."
apt-get update
apt-get install -y \
    gcc \
    python3-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    zlib1g-dev \
    libfreetype6-dev \
    build-essential

# Install Python packages
echo "📦 Installing Python packages..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Run migrations
echo "📦 Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "✅ Build complete!"
