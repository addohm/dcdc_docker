from django.contrib import admin
from .models import Staff, CarouselImage, Product, DiveSite, Social, Contact
from django.utils.timezone import now

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('description', 'image')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cost')

@admin.register(DiveSite)
class DiveSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'citystateprov', 'country', 'map_url')

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'when_sent', 'replied', 'when_replied' )
    readonly_fields = ('when_sent', 'when_replied')

    def save_model(self, request, obj, form, change):
        if 'replied' in form.changed_data:  # Check if 'replied' field was changed
            if obj.replied:
                obj.when_replied = now()  # Set when_replied to current datetime
            else:
                obj.when_replied = None  # Clear the when_replied field if unchecked
        super().save_model(request, obj, form, change)