#!/bin/bash
apt-get update && apt-get install -y libjpeg-dev libpng-dev
pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput
