from django.conf.urls.defaults import *

from beerdb.views import BeerDetailView, BeerListView, BrewerDetailView, BrewerListView, UserDetailView

urlpatterns = patterns('',
  # User ratings
  (r'^user/(?P<slug>[^/]+)/$', UserDetailView.as_view(), {}, 'beerdb_user_detail'),
  
  # Beers
  (r'^$', BeerListView.as_view(), {}, 'beerdb_beer_list'),
  (r'^(?P<brewer__slug>[^/]+)/(?P<slug>[^/]+)/$', BeerDetailView.as_view(), {}, 'beerdb_beer_detail'),
  
  # Brewers
  (r'^brewers/$', BrewerListView.as_view(), {}, 'beerdb_brewer_list'),
  (r'^(?P<slug>[^/]+)/$', BrewerDetailView.as_view(), {}, 'beerdb_brewer_detail'),
)