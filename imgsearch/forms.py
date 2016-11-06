from django import forms
from . import models


class PhotoForm(forms.Form):
    image = forms.ImageField()

