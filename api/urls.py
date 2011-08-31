from piston.resource import Resource

from django.conf.urls.defaults import *

from handlers import BeerHandler, BrewerHandler

beer_handler = Resource(BeerHandler)
brewer_handler = Resource(BrewerHandler)

urlpatterns = patterns('',
  # Beers
  (r'^beer/(?P<beer_slug>[^/]+?)(?:\.(?P<emitter_format>[a-z]+))?$', beer_handler, {}, 'beer'),
  (r'^beer(?:/|\.(?P<emitter_format>[a-z]+))?$', beer_handler, {}, 'beers'),
  
  # Brewers
  (r'^brewer/(?P<brewer_slug>[^/]+?)(?:\.(?P<emitter_format>[a-z]+))?$', brewer_handler, {}, 'brewer'),
  (r'^brewer(?:/|\.(?P<emitter_format>[a-z]+))?$', brewer_handler, {}, 'brewers'),
  
  # Documentation
  (r'^doc/$', 'piston.doc.documentation_view'),
)