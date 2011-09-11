from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView

from beerdb.models import Beer, Brewer

urlpatterns = patterns('',
  # Beers
  (r'^$', ListView.as_view(model=Beer), {}, 'beerdb_beer_list'),
  (r'^(?P<brewer__slug>[^/]+)/(?P<slug>[^/]+)/$', DetailView.as_view(model=Beer), {}, 'beerdb_beer_detail'),
  
  # Brewers
  (r'^brewers/$', ListView.as_view(model=Brewer), {}, 'beerdb_brewer_list'),
  (r'^(?P<slug>[^/]+)/$', DetailView.as_view(model=Brewer), {}, 'beerdb_brewer_detail'),
)