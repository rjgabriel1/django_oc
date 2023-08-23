from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        DANCE = 'DANCE'
        POP = 'POP'
        RNB = 'R&B'
        CHRISTIAN = 'CHRISTIAN'
        COUNTRY = 'COUNTRY'
        ROCK = 'ROCK'
        ELECTRONIC = 'ELECTRONIC'
        JAZZ = 'JAZZ'
        CLASSICAL = 'CLASSICAL'
        HEAVY_METAL = 'HM'
        INDIE = 'INDIE'
        FOLK = 'FOLK'
        REGGAE = 'REGGAE'
        BLUES = 'BLUES'
        LATIN = 'LATIN'
        FUNK = 'FUNK'
        PUNK = 'PUNK'
        DISCO = 'DISCO'
        HIPSTER = 'HIPSTER'
        GRUNGE = 'GRUNGE'
        TECHNO = 'TECHNO'
        COUNTRY_ROCK = 'COUNTRY_ROCK'
        TRAP = 'TRAP'
        SALSA = 'SALSA'
        SOUNDTRACK = 'SOUNDTRACK'
        PSYCHEDELIC = 'PSYCHEDELIC'
        RAP = 'RAP'
        GOSPEL = 'GOSPEL'
        NEW_WAVE = 'NEW_WAVE'
        EDM = 'EDM'
        TRANCE = 'TRANCE'
        EMO = 'EMO'
        FUSION = 'FUSION'
        ALTERNATIVE_POP = 'ALTERNATIVE_POP'
        SINGER_SONGWRITER = 'SINGER_SONGWRITER'
        RAGGAE = 'RAGGAE'
        HARD_ROCK = 'HARD_ROCK'
        SOUL = 'SOUL'
        RANCHERA = 'RANCHERA'
        ELECTRO_POP = 'ELECTRO_POP'
        SYMPHONIC = 'SYMPHONIC'
        REGGAETON = 'REGGAETON'
        BOLLYWOOD = 'BOLLYWOOD'

        
    name = models.CharField(max_length=100)
    genre = models.CharField(choices= Genre.choices, default='HH',max_length=25)
    biography = models.CharField(max_length=1000, default='')
    year_formed = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)], default=2000)
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name



class Merch(models.Model):
    class Type(models.TextChoices):
        record ='record'
        clothing = 'clothing'
        poster = 'poster'
        miscellaneous ='miscellaneous'
        
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500, default='')
    sold = models.BooleanField(default=False)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)])
    type = models.CharField(choices=Type.choices, max_length=50,default='Records')
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.description


class Song(models.Model):
    title =models.CharField(max_length=150)