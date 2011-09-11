from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView

from beerdb.models import Beer, Brewer

class BeerDetailView(DetailView):
  context_object_name = 'beer'
  model = Beer

class BeerListView(ListView):
  context_object_name = 'beers'
  model = Beer

class BrewerDetailView(DetailView):
  context_object_name = 'brewer'
  model = Brewer

class BrewerListView(ListView):
  context_object_name = 'brewers'
  model = Brewer

class UserDetailView(DetailView):
  context_object_name = 'user'
  model = User
  # Exclude site staff
  queryset = User.objects.exclude(is_staff=True)
  # Select user by username
  slug_field = 'username'