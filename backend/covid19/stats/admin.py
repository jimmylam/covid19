from django.contrib import admin
from .models import Country, Region, City, CountryStats, RegionStats, CityStats

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Country, LocationAdmin)
admin.site.register(Region, LocationAdmin)
admin.site.register(City, LocationAdmin)
admin.site.register(CountryStats)
admin.site.register(RegionStats)
admin.site.register(CityStats)
