from django import forms
from django.contrib.auth.models import User

from beerdb.models import Beer, Rating, UserRating

class UserRatingForm(forms.ModelForm):
  delete = forms.BooleanField(required=False)
  
  class Meta:
    model = UserRating
    fields = ('beer', 'user', 'rating', 'note')
    widgets = {
      'beer': forms.HiddenInput(),
      'user': forms.HiddenInput(),
    }
  
  def save(self, *args, **kwargs):
    # Delete if user chose to delete rating or if no rating is set and note is empty
    if (self.instance.id and self.cleaned_data['delete']) or (self.cleaned_data['rating'] == None and len(self.cleaned_data['note']) == 0):
      # Delete the current instance
      self.instance.delete()
      # Return an empty instance
      instance = UserRating.objects.none()
    else:
      # Default instance creation/update
      instance = super(UserRatingForm, self).save(*args, **kwargs)
    
    return instance

class SearchForm(forms.Form):
  query = forms.CharField(max_length=100)