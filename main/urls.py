#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin


admin.autodiscover()

urlpatterns = i18n_patterns("",
    ("^manage/", include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),
    ("^", include("mezzanine.urls")),
)


handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
