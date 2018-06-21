#!/bin/bash

python3 ./website/manage.py makemigrations

python3 ./website/manage.py migrate
