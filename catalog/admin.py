from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from catalog.models import Brand, Site, Widget


class BrandModelAdmin(admin.ModelAdmin):
    search_fields = 'title', 'sites__domain',


class SiteModelAdmin(admin.ModelAdmin):
    search_fields = 'domain', 'widgets__title',


class WidgetModelAdmin(admin.ModelAdmin):
    search_fields = 'title',
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


admin.site.register(Brand, BrandModelAdmin)
admin.site.register(Site, SiteModelAdmin)
admin.site.register(Widget, WidgetModelAdmin)
