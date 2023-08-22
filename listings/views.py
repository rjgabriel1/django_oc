from django.http import HttpResponse
from django.shortcuts import redirect, render
from listings.models import Band, Merch
from listings.forms import ContactForm, BandForm, MerchForm
from django.core.mail import send_mail

# Create your views here.


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'bands/band_list.html',
                  {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
                  'bands/band_detail.html',
                  {'band': band}
                  )


def band_add(request):
    if request.method =="POST":
        form = BandForm(request.POST)
        if form.is_valid():
            #create new band and add it to the db.
            band = form.save()
        return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'bands/band_add.html', {'form': form})



def merch_list(request):
    merchs = Merch.objects.all()
    return render(request, 'bands/merch_list.html', {'merchs': merchs})


def merch_detail(request, merch_id):
    merch = Merch.objects.get(id=merch_id)
    return render(request, 'bands/merch_detail.html', {'merch': merch})

def merch_add(request):
    if request.method == 'POST':
        form = MerchForm(request.POST)
        if form.is_valid():
           merch = form.save()
           return redirect('merch-detail', merch.id)
    else:
        form = MerchForm()
    return render(request, 'bands/merch_add.html', {'form': form})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            send_mail(subject=f"Message from {form.cleaned_data['name']} Merchex  contact form",
                      message=form.cleaned_data['message'],
                      from_email=form.cleaned_data['email'],
                      recipient_list=['admin@example.com']
                      )
            return redirect('email_sent.html')
    else:
        form = ContactForm()
    return render(request, 'bands/contact.html', {"form": form})


def email_sent(request):
    return render(request, 'bands/email_sent.html')
