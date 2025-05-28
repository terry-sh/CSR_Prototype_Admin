from datetime import datetime
from django.contrib import admin

from ..models.activity_enroll import ActivityEnroll

class ActivityEnrollAdmin(admin.ModelAdmin):
    list_display = ('activity_name', 'user_name', 'status',)
    fields = ('activity', 'user', 'enroll_time', 'status', 'approve_time', 'approver',)
    search_fields = ('activity', 'user', 'status',)
    ordering = ('enroll_time',)

    def get_readonly_fields(self, request, obj=None):
        fields = ['activity', 'user', 'enroll_time', 'approve_time', 'approver']
        if obj is not None and not request.user.is_superuser:
           fields.append('status')
        return fields

    def save_model(self, request, obj, form, change):
        if change:
            if 'status' in form.changed_data:
                obj.approver = request.user
                obj.approve_time = datetime.now()
        super().save_model(request, obj, form, change)

admin.site.register(ActivityEnroll, ActivityEnrollAdmin)
