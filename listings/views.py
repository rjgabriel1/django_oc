from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Song
# Create your views here.


def band_list(request):
    bands = Band.objects.all()
    song = Song.objects.all()
    return render(request,
        'bands/band_list.html',
        {'bands': bands})


def about(request):
    return render(request,'bands/about.html')
