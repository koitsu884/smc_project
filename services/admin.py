from django.contrib import admin

from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_ja', 'title_ko', 'title_zh', 'display_top')
    list_editable = ('display_top',)
    pass

admin.site.register(Service, ServiceAdmin)
