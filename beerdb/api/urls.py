from piston.resource import Resource

from django.conf.urls.defaults import *

from handlers import BeerHandler, BrewerHandler, UserHandler

beer_handler = Resource(BeerHandler)
brewer_handler = Resource(BrewerHandler)
user_handler = Resource(UserHandler)

urlpatterns = patterns('',
  # Documentation
  (r'^doc/$', 'piston.doc.documentation_view'),

  # Listing of all brewers
  (r'^brewers/$', brewer_handler, {'emitter_format': 'json'}, 'beerdb_api_brewers'),
  
  # Listing of all beers
  (r'^beers/$', beer_handler, {'emitter_format': 'json'}, 'beerdb_api_beers'),
  
  # User ratings
  (r'^user/(?P<username>[^/]+)/$', user_handler, {'emitter_format': 'json'}, 'beerdb_api_user'),
  
  # Specific brewer listing
  (r'^(?P<brewer_slug>[^/]+)/$', brewer_handler, {'emitter_format': 'json'}, 'beerdb_api_brewer'),
  
  # Specific beer listing
  (r'^(?P<brewer_slug>[^/]+)/(?P<beer_slug>[^/]+)/$', beer_handler, {'emitter_format': 'json'}, 'beerdb_api_beer'),
)