#!/usr/bin/python
# -*- coding: utf-8 -*-


import os


settings_module = "main.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)


from django.contrib.auth import get_user_model


User = get_user_model()


if User.objects.count() == 0:
    # Admin user
    admin = User.objects.create(username='admin')
    admin.set_password('admin')
    admin.email = 'admin@ictac2015.co'
    admin.first_name = 'ICTAC 2015'
    admin.last_name = 'Website Administrator'
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()
    # Editor user
    editor = User.objects.create(username='editor')
    editor.set_password('editor')
    editor.email = 'contact@ictac2015.co'
    editor.first_name = 'ICTAC 2015'
    editor.last_name = 'Organizing Committee'
    editor.is_staff = True
    editor.save()
