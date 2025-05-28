from django.contrib import admin

from ..models.event import ActivityEvent, ActivityEventTranslation

class ActivityEventTranslationInline(admin.TabularInline):
    model = ActivityEventTranslation
    fields = ('language', 'name', 'description')

class ActivityEventAdmin(admin.ModelAdmin):
    list_display = ('activity', 'name',)
    fields = ('activity', 'name', 'maximum_times', 'inactive_icon', 'active_icon',)
    search_fields = ('activity', 'name',)
    ordering = ('activity',)
    inlines = [ActivityEventTranslationInline]

admin.site.register(ActivityEvent, ActivityEventAdmin)
