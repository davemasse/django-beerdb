from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView

from beerdb.models import Beer, Brewer

urlpatterns = patterns('',
  # Beers
  (r'^beer/$', ListView.as_view(model=Beer), {}, 'beerdb_beer_list'),
  (r'^beer/(?P<slug>[^/]+)/$', DetailView.as_view(model=Beer), {}, 'beerdb_beer_detail'),
  
  # Brewers
  (r'^brewer/$', ListView.as_view(model=Brewer), {}, 'beerdb_brewer_list'),
  (r'^brewer/(?P<slug>[^/]+)/$', DetailView.as_view(model=Brewer), {}, 'beerdb_brewer_detail'),
  
  (r'^api/', include('beerdb.api.urls')),
)