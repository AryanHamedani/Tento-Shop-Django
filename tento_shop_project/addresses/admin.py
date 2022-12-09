from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from tento_shop_project.addresses.models import Address, City, Province


@admin.register(Address)
class AddressAdmin(OSMGeoAdmin):
    list_display = (
        "title",
        "street",
        "number",
        "unit",
        "postal_code",
        "location",
        "owner",
    )


admin.site.register(City)
admin.site.register(Province)
