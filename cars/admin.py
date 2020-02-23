from django.contrib import admin
from django.utils.html import format_html

from .models import Car, CarModel, Manufacturer, Feature, Image


class PhotoInline(admin.StackedInline):
    model = Image
    extra = 1
    readonly_fields =['image_current']

    def image_current(self, obj):
        return format_html('<img src="{}" class="thumbnail"  />'.format(obj.image.url))


class CarAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    readonly_fields = ['main_image_current']
    raw_id_fields = ['model']

    def main_image_current(self, obj):
        return format_html('<img src="{}" class="thumbnail"  />'.format(obj.photo_main.url))

    # def save_model(self, request, obj, form, change):
    #     obj.save()

    #     for afile in request.FILES.getlist('photos_multiple'):
    #         obj.photos.create(image=afile)


class CarModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'manufacturer__name']
    pass


class ManufacturerAdmin(admin.ModelAdmin):
    pass


class FeatureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Car, CarAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Feature, FeatureAdmin)
