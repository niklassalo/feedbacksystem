from django.contrib import admin
from .models import Topic, Feedback

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'topic', 'grade', 'date']
    list_filter = ['topic', 'grade']
    search_fields = ['user__username', 'topic__name']
    date_hierarchy = 'date'

admin.site.register(Topic)
admin.site.register(Feedback)
