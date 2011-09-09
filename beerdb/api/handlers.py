from piston.emitters import Emitter, JSONEmitter
from piston.handler import BaseHandler

from django.core.urlresolvers import reverse

from beerdb.models import Beer, Brewer, Rating, URL, URLSite

class BeerHandler(BaseHandler):
  allowed_methods = ('GET',)
  fields = ('name', 'url', ('brewer', ('name',)), ('userbeer_set', ('note', 'date_added', ('user', ('username',)), ('rating', ('name',)))))
  model = Beer
  
  def read(self, request, brewer_slug=None, beer_slug=None):
    if brewer_slug and beer_slug:
      try:
        return Beer.objects.get(brewer__slug=brewer_slug, slug=beer_slug)
      except Beer.DoesNotExist:
        return Beer.objects.none()
    else:
      beers = Beer.objects.all()[:10]
      
      for beer in beers:
        beer.ratings = beer.userbeer_set.all()
        beer.name = 'test'
      return beers

class BrewerHandler(BaseHandler):
  allowed_methods = ('GET',)
  fields = ('name', 'beer')
  model = Brewer
  
  def read(self, request, brewer_slug=None):
    if brewer_slug:
      try:
        return Brewer.objects.get(slug=brewer_slug)
      except Brewer.DoesNotExist:
        return Brewer.objects.none()
    else:
      self.fields = ('name')
      return Brewer.objects.all()[:10]
  
  @classmethod
  def beer(self, object):
    return object.beer_set.all()

class URLSiteHandler(BaseHandler):
  allowed_methods = ()
  model = URLSite

class URLHandler(BaseHandler):
  allowed_methods = ()
  model = URL