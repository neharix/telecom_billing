from django.contrib import admin

from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["full_name", "phone_number", "balance"]
    readonly_fields = ("id",)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    readonly_fields = ("id",)


@admin.register(Appraisal)
class AppraisalAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    readonly_fields = ("id",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    readonly_fields = ("id",)
