from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView

from beer_db.models import Beer, Brewer

urlpatterns = patterns('',
  # Beers
  (r'^beer/$', ListView.as_view(model=Beer), {}, 'beer_db_beer_list'),
  (r'^beer/(?P<slug>[^/]+)/$', DetailView.as_view(model=Beer), {}, 'beer_db_beer_detail'),
  
  # Brewers
  (r'^brewer/$', ListView.as_view(model=Brewer), {}, 'beer_db_brewer_list'),
  (r'^brewer/(?P<slug>[^/]+)/$', DetailView.as_view(model=Brewer), {}, 'beer_db_brewer_detail'),
  
  (r'^api/', include('beer_db.api.urls')),
)