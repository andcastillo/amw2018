#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import absolute_import, unicode_literals

import os


PRO_ENV = os.environ.get('PRO_ENV', False)


CURRENT_FOLDER = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_FOLDER, os.pardir))
PROJECT_DIRNAME = CURRENT_FOLDER.split(os.sep)[-1]


# -------------------------------------------------
# Mezzanine settings
# -------------------------------------------------


ADMIN_MENU_ORDER = (
    ("Content", (
        "pages.Page", "blog.BlogPost", "utils.RightPanelSection", #"generic.ThreadedComment",
        #("Media Library", "fb_browse"),  # TODO: Temporal while bugs gets fixed.
    )),
    ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
    ("Users", ("auth.User", "auth.Group",)),
)


PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"


OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)


USE_SOUTH = False


COMMENTS_ACCOUNT_REQUIRED = True
COMMENTS_DEFAULT_APPROVED = False
COMMENTS_REMOVED_VISIBLE = False
COMMENTS_UNAPPROVED_VISIBLE = False
COMMENTS_USE_RATINGS = False


# -------------------------------------------------
# Django settings
# -------------------------------------------------


ADMINS = (
    ('Julián Pérez', 'jcpmmx@gmail.com'),
)
MANAGERS = ADMINS


SECRET_KEY = "93cbdeb8-b56e-4f4f-81da-9f554904e0e126aaebeb-30f3-41f6-becf-412826eb7b801941db05-277e-4206-a5fd-54a17e5c2b2e"
NEVERCACHE_KEY = "c81e2802-dec6-4316-900e-11924e5c4de99899a9dc-58fb-4065-87c1-82919587e4b61b21ada4-a05f-4b61-ac92-c5db7fb63ab5"


TIME_ZONE = 'America/Bogota'
USE_TZ = True

LANGUAGE_CODE = "en"

_ = lambda s: s
LANGUAGES = (
    ('en', _('English')),
)


SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SITE_ID = 1

USE_I18N = False

INTERNAL_IPS = ("127.0.0.1",)


TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

AUTHENTICATION_BACKENDS = (
    "mezzanine.core.auth_backends.MezzanineBackend",
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

FILE_UPLOAD_PERMISSIONS = 0o644


CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME


STATIC_URL = "/static/"
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, STATIC_URL.strip("/")),
)

MEDIA_URL = STATIC_URL + "media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, MEDIA_URL.strip("/"))


ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME


TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)


INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "storages",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.pages",
    "mezzanine.galleries",
    "main.utils"
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "mezzanine.conf.context_processors.settings",
    "mezzanine.pages.context_processors.page",
    "main.utils.context_processors.right_panel_sections"
)


MIDDLEWARE_CLASSES = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)


# -------------------------------------------------
# Environment-based settings
# -------------------------------------------------


if PRO_ENV:
    try:
        from main.settings_pro import *
    except ImportError:
        raise ImportError(u"Missing file settings_pro.py is required.")
else:
    try:
        from main.settings_dev import *
    except ImportError:
        raise ImportError(u"Missing file settings_dev.py is required.")


# -------------------------------------------------
# Mezzanine dynamic settings
# -------------------------------------------------


try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
