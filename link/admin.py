from django.contrib import admin

from link.models import ContactModel, SocialLinkModel, BannerModel


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'full_name', 'email', 'created_date')
    readonly_fields = ('id', 'title', 'full_name', 'email', 'created_date', 'message')

@admin.register(SocialLinkModel)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url',)

@admin.register(BannerModel)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'is_active')
