from django.contrib import admin
from listings.models import Band

# Register your models here.
class BandAndmin(admin.ModelAdmin):
    # fields to display in admin panel
    list_display = ('name','year_formed', 'genre')
    
    
admin.site.register(Band,BandAndmin)