from piston.resource import Resource

from django.conf.urls.defaults import *

from handlers import BeerHandler, BrewerHandler

beer_handler = Resource(BeerHandler)
brewer_handler = Resource(BrewerHandler)

urlpatterns = patterns('',
  # Beers
  (r'^(?P<brewer_slug>[^/]+)/(?P<beer_slug>[^/]+)/$', beer_handler, {}, 'beerdb_api_beer'),
  (r'^beer/$', beer_handler, {}, 'beerdb_api_beers'),
  
  # Brewers
  (r'^(?P<brewer_slug>[^/]+)/$', brewer_handler, {}, 'beerdb_api_brewer'),
  (r'^brewer/$', brewer_handler, {}, 'beerdb_api_brewers'),
  
  # Documentation
  (r'^doc/$', 'piston.doc.documentation_view'),
)