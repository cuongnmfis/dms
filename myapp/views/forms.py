from django import forms
from django.forms import ModelForm


class AdvertForm(ModelForm):
    class Meta:
        model = Advert