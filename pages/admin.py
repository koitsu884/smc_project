from django.contrib import admin

from .models import Feedback, ContactDetail


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('title','email', 'content', 'timestamp')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class ContactDetailAdmin(admin.ModelAdmin):
    list_display = (
        'mobile',
        'phone', 
        'email', 
        'opening_hour_mon',
        'opening_hour_tue',
        'opening_hour_wed',
        'opening_hour_thu',
        'opening_hour_fri',
        'opening_hour_sat',
        'opening_hour_sun',
        
        )
    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(ContactDetail, ContactDetailAdmin)
