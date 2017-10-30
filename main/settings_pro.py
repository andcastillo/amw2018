#!/usr/bin/python
# -*- coding: utf-8 -*-


import os


DEBUG = False


ALLOWED_HOSTS = [
    'ictac2015-env-ir4bwfjpb5.elasticbeanstalk.com',
    '.ictac2015.co'
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD']
    }
}


LOGGING = {
    'version': 1,
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    },
}


S3_URL_BASE = 'http://%s.s3.amazonaws.com' % os.environ['AWS_S3_BUCKET_NAME']
STATIC_URL = '%s/static/' % S3_URL_BASE
MEDIA_URL = '%s/media/' % STATIC_URL


DEFAULT_FILE_STORAGE = 'main.utils.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'main.utils.s3utils.StaticRootS3BotoStorage'


AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_S3_BUCKET_NAME']
AWS_PRELOAD_METADATA = True
