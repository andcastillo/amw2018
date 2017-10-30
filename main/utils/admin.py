#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.comments.admin import CommentsAdmin

from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin
from mezzanine.generic.admin import ThreadedCommentAdmin
from mezzanine.generic.models import ThreadedComment

from .models import RightPanelSection


class RightPanelSectionAdmin(DisplayableAdmin):
    """
    Admin interface for RightPanelSection model.
    """
    fieldsets = (
        (None, {
            "fields": ["title", "status", ("publish_date", "expiry_date"), "content"],
        }),
    )


class CustomThreadedCommentAdmin(ThreadedCommentAdmin):
    """
    Admin interface for ThreadedComment model.
    """

    def get_actions(self, request):
        actions = super(CommentsAdmin, self).get_actions(request)
        actions.pop('flag_comments')
        return actions


admin.site.register(RightPanelSection, RightPanelSectionAdmin)

admin.site.unregister(ThreadedComment)
generic_comments = getattr(settings, "COMMENTS_APP", "") == "mezzanine.generic"
if generic_comments and not settings.COMMENTS_DISQUS_SHORTNAME:
    admin.site.register(ThreadedComment, CustomThreadedCommentAdmin)
