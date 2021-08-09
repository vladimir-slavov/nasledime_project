from django.contrib import admin

from nasledime_project.nasledime.models import Will


class WillAdmin(admin.ModelAdmin):
    pass


admin.site.register(Will, WillAdmin)
