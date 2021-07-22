from django.contrib import admin
from catalog.models import Brand, Site, Widget, WidgetConfigurationItem


class BrandModelAdmin(admin.ModelAdmin):
    search_fields = 'title', 'sites__domain',


class SiteModelAdmin(admin.ModelAdmin):
    search_fields = 'domain', 'widgets__title',


class WidgetConfigurationItemInline(admin.TabularInline):
    model = WidgetConfigurationItem
    extra = 1


class WidgetModelAdmin(admin.ModelAdmin):
    search_fields = 'title',
    inlines = [WidgetConfigurationItemInline, ]


admin.site.register(Brand, BrandModelAdmin)
admin.site.register(Site, SiteModelAdmin)
admin.site.register(Widget, WidgetModelAdmin)
admin.site.register(WidgetConfigurationItem)
