from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP ='HH' 
        SYNTH_POP ='SP'
        AR = 'AR' 
        
    name = models.CharField(max_length=100)
    genre = models.CharField(choices= Genre.choices, default='HH',max_length=5)
    biography = models.CharField(max_length=1000, default='')
    year_formed = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)], default=2000)
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)



class Merch(models.Model):
    class Type(models.TextChoices):
        record ='record'
        clothing = 'clothing'
        poster = 'poster'
        miscellaneous ='miscellaneous'
        
    description = models.CharField(max_length=500, default='')
    sold = models.BooleanField(default=False)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)])
    type = models.CharField(choices=Type.choices, max_length=50,default='Records')




class Song(models.Model):
    title =models.CharField(max_length=150)