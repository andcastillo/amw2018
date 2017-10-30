#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from .models import RightPanelSection


def right_panel_sections(request):
    """
    Returns a list of all Right panel sections available.
    """
    return {
        'right_panel_sections': RightPanelSection.objects.published(for_user=request.user)
    }
