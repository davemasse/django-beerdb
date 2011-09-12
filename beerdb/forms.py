from django import forms
from django.contrib.auth.models import User

from beerdb.models import Beer, Rating, UserRating

class UserRatingForm(forms.ModelForm):
  class Meta:
    model = UserRating
    fields = ('beer', 'user', 'rating', 'note')
    widgets = {
      'beer': forms.HiddenInput(),
      'user': forms.HiddenInput(),
    }

class SearchForm(forms.Form):
  query = forms.CharField(max_length=100)