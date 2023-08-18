from django.contrib import admin
from listings.models import Band,Merch

# Register your models here.
class BandAndmin(admin.ModelAdmin):
    # fields to display in admin panel
    list_display = ('name','year_formed', 'genre')

class MerchAdmin(admin.ModelAdmin):
    list_display = ('description', 'band','sold','type','year')

# register Band model
admin.site.register(Band,BandAndmin)

# register Merch model
admin.site.register(Merch,MerchAdmin)