from django import forms
from django.contrib.auth.models import User

from beerdb.models import Beer, Rating, UserRating

class UserRatingForm(forms.ModelForm):
  beer = forms.CharField(widget=forms.HiddenInput())
  user = forms.CharField(widget=forms.HiddenInput())
  
  class Meta:
    model = UserRating
    fields = ('beer', 'user', 'rating', 'note')
  
  def clean_beer(self):
    beer_id = self.cleaned_data.get('beer')
    
    try:
      beer = Beer.objects.get(id=beer_id)
    except Beer.DoesNotExist:
      beer = Beer.objects.none()
    
    return beer
  
  def clean_user(self):
    user_id = self.cleaned_data.get('user')
    
    try:
      user = User.objects.get(id=user_id)
    except User.DoesNotExist:
      user = User.objects.none()
    
    return user

class SearchForm(forms.Form):
  query = forms.CharField(max_length=100)