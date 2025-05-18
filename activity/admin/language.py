from django.contrib import admin

from ..models.language import Language

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'native_name', 'status', 'sort')
    fields = ('code', 'native_name', 'status', 'sort')
    search_fields = ('code', 'native_name')
    ordering = ('sort',)

admin.site.register(Language, LanguageAdmin)
