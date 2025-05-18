from django.contrib import admin

from ..models.activity import Activity, ActivityTranslation

class ActivityTranslationInline(admin.TabularInline):
    model = ActivityTranslation
    fields = ('language', 'name', 'introduction')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'location', 'status')
    fields = ('name', 'code', 'cover_image', 'start_date', 'end_date', 'location', 'geo_location', 'status')
    search_fields = ('short_name', 'location')
    ordering = ('start_date',)
    inlines = [ActivityTranslationInline]

admin.site.register(Activity, ActivityAdmin)
