#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

import os


settings_module = "main.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
