FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=hospital_api.settings

RUN apt-get update && apt-get install -y \
    gcc libjpeg-dev libpng-dev libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .

# Create admin setup script
RUN echo "import os; import django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_api.settings'); django.setup(); from django.contrib.auth import get_user_model; User = get_user_model(); user, created = User.objects.get_or_create(username='admin', defaults={'email':'admin@hospital.com'}); user.set_password('hospital123'); user.is_superuser=True; user.is_staff=True; user.save(); print('✅ Admin: admin / hospital123')" > /setup_admin.py

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && python /setup_admin.py && gunicorn hospital_api.wsgi:application"]
