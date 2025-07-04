#!/usr/bin/env bash

# aplică migrațiile
python manage.py migrate

# colectează fișierele statice
python manage.py collectstatic --noinput
