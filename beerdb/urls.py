from django.conf.urls.defaults import *
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView

from beerdb.models import Beer, Brewer

urlpatterns = patterns('',
  # User ratings
  (r'^user/(?P<slug>[^/]+)/$', DetailView.as_view(model=User, slug_field='username', context_object_name='user'), {}, 'beerdb_user_detail'),
  
  # Beers
  (r'^$', ListView.as_view(model=Beer, context_object_name='beers'), {}, 'beerdb_beer_list'),
  (r'^(?P<brewer__slug>[^/]+)/(?P<slug>[^/]+)/$', DetailView.as_view(model=Beer, context_object_name='beer'), {}, 'beerdb_beer_detail'),
  
  # Brewers
  (r'^brewers/$', ListView.as_view(model=Brewer, context_object_name='brewers'), {}, 'beerdb_brewer_list'),
  (r'^(?P<slug>[^/]+)/$', DetailView.as_view(model=Brewer, context_object_name='brewer'), {}, 'beerdb_brewer_detail'),
)