from piston.resource import Resource

from django.conf.urls.defaults import *

from handlers import BeerHandler, BrewerHandler

beer_handler = Resource(BeerHandler)
brewer_handler = Resource(BrewerHandler)

urlpatterns = patterns('',
  # Documentation
  (r'^doc/$', 'piston.doc.documentation_view'),

  # Listing of all brewers
  (r'^brewers/$', brewer_handler, {}, 'beerdb_api_brewers'),
  
  # Listing of all beers
  (r'^beers/$', beer_handler, {}, 'beerdb_api_beers'),
  
  # Specific brewer listing
  (r'^(?P<brewer_slug>[^/]+)/$', brewer_handler, {}, 'beerdb_api_brewer'),
  
  # Specific beer listing
  (r'^(?P<brewer_slug>[^/]+)/(?P<beer_slug>[^/]+)/$', beer_handler, {}, 'beerdb_api_beer'),
)