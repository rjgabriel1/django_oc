from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Song
# Create your views here.


def hello(request):
    bands = Band.objects.all()
    song = Song.objects.all()
    return render(request,
        'bands/hello.html',
        {'bands': bands})


def about(request):
    return render(request,'bands/about.html')
