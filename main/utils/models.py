#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.models import Displayable, RichText


class RightPanelSection(Displayable, RichText):
    """
    Model that represents a static but editable section that will appear in the right panel.
    """
    titles = models.CharField(editable=False, max_length=1000, null=True)

    class Meta:
        verbose_name = _("Right panel section")
        verbose_name_plural = _("Right panel sections")
        ordering = ("titles",)

    def __str__(self):
        return self.titles

    def get_absolute_url(self):
        pass
