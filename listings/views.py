from django.http import HttpResponse
from django.shortcuts import redirect, render
from listings.models import Band, Merch
from listings.forms import ContactForm, BandForm, MerchForm
from django.core.mail import send_mail

# Band Views

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
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            # create new band and add it to the db.
            band = form.save()
        return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'bands/band_add.html', {'form': form})


def band_update(reuqest, band_id):
    band = Band.objects.get(id=band_id)
    if reuqest.method == "POST":
        form = BandForm(reuqest.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(reuqest, 'bands/band_update.html', {'form': form})


def band_delete(request, band_id):
    band = Band.objects.get(id= band_id)
    if request.method == "POST":
        band.delete()
        return redirect('band-list')
    
    return render(request,'bands/band_delete.html',{"band":band})


# Merch Views

def merch_list(request):
    merchs = Merch.objects.all()
    return render(request, 'merch/merch_list.html', {'merchs': merchs})


def merch_detail(request, merch_id):
    merch = Merch.objects.get(id=merch_id)
    return render(request, 'merch/merch_detail.html', {'merch': merch})


def merch_add(request):
    if request.method == 'POST':
        form = MerchForm(request.POST)
        if form.is_valid():
            merch = form.save()
            return redirect('merch-detail', merch.id)
    else:
        form = MerchForm()
    return render(request, 'merch/merch_add.html', {'form': form})


def merch_update(request, merch_id):
    merch = Merch.objects.get(id =merch_id)
    
    if request =="POST":
        form = MerchForm(request.POST, instance=merch)
        if form.is_valid():
            form.save()
            return redirect('merch-detail', merch.id)
    
    else:
        form = MerchForm(instance=merch)
    
    return render(request, 'merch/merch_update.html', {'form': form})
    
# Other Views
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
