# settings/development.py
import os
from pathlib import Path
from dotenv import load_dotenv
from .base import * # Importa lo común de base.py

load_dotenv()

# Punto 5: Implementación de variables
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}