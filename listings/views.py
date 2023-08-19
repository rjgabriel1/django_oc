from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Merch

# Create your views here.


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'bands/band_list.html',
                  {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id = band_id)
    return render(request,
                  'bands/band_detail.html',
                  {'band': band}
                  )

# 
def merch_list(request):
    merchs = Merch.objects.all()
    return render(request,'bands/merch_list.html',{'merchs': merchs})


def merch_detail(request, merch_id):
    merch = Merch.objects.get(id=merch_id)
    return render(request,'bands/merch_detail.html',{'merch': merch})


def about(request):
    return render(request, 'bands/about.html')
