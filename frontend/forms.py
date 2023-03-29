from django import forms
from django.forms import Modelform
from .models import Venue

class Venueform(Modelform):
    class Meta:
        model = Venue
        fields = ('venue_image')
        labels = {
            'venue_image': '',
        }
