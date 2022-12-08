from django.contrib import admin

from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Class for feedback admin panel."""

    list_display = ('text',)
