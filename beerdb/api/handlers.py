from piston.emitters import Emitter, JSONEmitter
from piston.handler import BaseHandler

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from beerdb.models import Beer, Brewer, Rating, URL, URLSite

class BeerHandler(BaseHandler):
  allowed_methods = ('GET',)
  fields = ('name', 'url', ('brewer', ('name',)), ('userbeer_set', ('note', 'date_added', ('user', ('username',)), ('rating', ('name',)))))
  model = Beer
  
  def read(self, request, brewer_slug=None, beer_slug=None):
    if brewer_slug and beer_slug:
      try:
        data = Beer.objects.get(brewer__slug=brewer_slug, slug=beer_slug)
      except Beer.DoesNotExist:
        data = Beer.objects.none()
    else:
      data = Beer.objects.all()[:10]
    
    return data

class BrewerHandler(BaseHandler):
  allowed_methods = ('GET',)
  fields = ('name', 'beer')
  model = Brewer
  
  def read(self, request, brewer_slug=None):
    if brewer_slug:
      try:
        data = Brewer.objects.get(slug=brewer_slug)
      except Brewer.DoesNotExist:
        data = Brewer.objects.none()
    else:
      self.fields = ('name')
      data = Brewer.objects.all()[:10]
    
    return data
  
  @classmethod
  def beer(self, object):
    return object.beer_set.all()

class URLSiteHandler(BaseHandler):
  allowed_methods = ()
  model = URLSite

class URLHandler(BaseHandler):
  allowed_methods = ()
  model = URL

class UserHandler(BaseHandler):
  allowed_methods = ('GET',)
  fields = ('username', ('userbeer_set', ('note', 'date_added', ('beer', ('url', 'name', ('brewer', ('name',)))), ('rating', ('name',)))))
  model = User
  
  def read(self, request, username=None):
    if username:
      try:
        user = User.objects.exclude(is_staff=True).get(username=username)
      except User.DoesNotExist:
        user = User.objects.none()
    else:
      user = User.objects.none()
    
    return user