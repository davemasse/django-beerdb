from django.conf.urls.defaults import *

from beerdb.views import BeerDetailView, BeerListView, BrewerDetailView, BrewerListView, UserDetailView, beer_rate

urlpatterns = patterns('',
  # User ratings
  (r'^user/(?P<slug>[^/]+)/$', UserDetailView.as_view(), {}, 'beerdb_user_detail'),
  
  # Beers
  (r'^$', BeerListView.as_view(), {}, 'beerdb_beer_list'),
  (r'^(?P<brewer__slug>[^/]+)/(?P<slug>[^/]+)/$', BeerDetailView.as_view(), {}, 'beerdb_beer_detail'),
  (r'^(?P<brewer_slug>[^/]+)/(?P<beer_slug>[^/]+)/rate/$', beer_rate, {}, 'beerdb_beer_rate'),
  
  # Brewers
  (r'^brewers/$', BrewerListView.as_view(), {}, 'beerdb_brewer_list'),
  (r'^(?P<slug>[^/]+)/$', BrewerDetailView.as_view(), {}, 'beerdb_brewer_detail'),
)