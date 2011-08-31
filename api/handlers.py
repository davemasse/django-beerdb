from piston.emitters import Emitter, JSONEmitter
from piston.handler import BaseHandler

from django.core.urlresolvers import reverse

from beer_db.models import Beer, Brewer, URL, URLSite

class BeerHandler(BaseHandler):
  allowed_methods = ('GET',)
  fields = ('name', 'slug', ('brewer', ('name', 'slug')), 'url')
  model = Beer
  
  def read(self, request, beer_slug=None):
    if beer_slug:
      try:
        return Beer.objects.get(slug=beer_slug)
      except Beer.DoesNotExist:
        return Beer.objects.none()
    else:
      return Beer.objects.all()[:10]
  
  @classmethod
  def resource_uri(self):
    return ('beer', ['slug'])

class BrewerHandler(BaseHandler):
  allowed_methods = ('GET',)
  fields = ('name', 'slug', 'beer')
  model = Brewer
  
  @classmethod
  def resource_uri(self):
    return ('brewer', ['slug'])
  
  def read(self, request, brewer_slug=None):
    if brewer_slug:
      try:
        return Brewer.objects.get(slug=brewer_slug)
      except Brewer.DoesNotExist:
        return Brewer.objects.none()
    else:
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