from django.contrib import admin

from ..models.unit import Unit, UnitTranslation

class UnitTranslationInline(admin.TabularInline):
    model = UnitTranslation
    fields = ('language', 'name', 'format_template')

class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr',)
    fields = ('name', 'abbr',)
    search_fields = ('name', 'abbr')
    ordering = ('abbr',)
    inlines = [UnitTranslationInline]


admin.site.register(Unit, UnitAdmin)
