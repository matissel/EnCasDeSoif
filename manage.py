#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv


def verifyEnvIsSet():
    load_dotenv()
    MAPBOX_PRIVATE_KEY = os.getenv('MAPBOX_PRIVATE_KEY')
    MAPBOX_LOGIN = os.getenv('MAPBOX_LOGIN')
    if MAPBOX_PRIVATE_KEY == '' or MAPBOX_LOGIN == '':
        print('Set your mapbox api key and login in .env file')
        sys.exit()


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EnCasDeSoif.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    verifyEnvIsSet()
    main()
