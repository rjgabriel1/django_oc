from django import forms
from listings.models import Band, Merch


class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ["name",
                  "genre",
                  "biography",
                  "year_formed",
                  "active",
                  "official_homepage"
                  ]


class MerchForm(forms.ModelForm):
    class Meta:
        model = Merch
        fields = '__all__'
        exclude = ('sold',)
