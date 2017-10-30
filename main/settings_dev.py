#!/usr/bin/python
# -*- coding: utf-8 -*-


DEBUG = True


ALLOWED_HOSTS = [
    'localhost'
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "ictac2015",
        "USER": "ictac2015",
        "PASSWORD": "ictac2015"
    }
}
