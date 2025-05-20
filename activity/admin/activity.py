from django.contrib import admin

from ..models.activity import Activity, ActivityTranslation

class ActivityTranslationInline(admin.TabularInline):
    model = ActivityTranslation
    fields = ('language', 'name', 'slogan', 'location')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'status')
    fields = ('name', 'code', 'cover_image', 'start_date', 'end_date', 'geo_location', 'status')
    search_fields = ('short_name', 'name')
    ordering = ('start_date',)
    inlines = [ActivityTranslationInline]


class ActivityTranslationAdmin(admin.ModelAdmin):
    list_display = ('activity', 'language', 'name', 'slogan')
    fields = ('activity', 'language', 'name', 'slogan', 'location', 'introduction')

admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityTranslation, ActivityTranslationAdmin)
