from autoslug.fields import AutoSlugField

from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

class Rating(models.Model):
  slug = AutoSlugField(populate_from='name', unique=True, default='', help_text=_('Slug value for the rating.'))
  name = models.CharField(max_length=100, unique=True, help_text=_('Name of the rating for display purposes.'))
  order = models.PositiveIntegerField(unique=True, help_text=_('The order in which ratings are displayed.'))
  
  class Meta:
    ordering = ('order',)
    verbose_name = _('rating')
    verbose_name_plural = _('ratings')
  
  def __unicode__(self):
    return self.name

class URLSite(models.Model):
  name = models.CharField(max_length=250, help_text=_('The display name for the domain.'))
  domain = models.CharField(max_length=250, help_text=_('The domain of the related site.'))
  
  class Meta:
    verbose_name = _('URL site')
    verbose_name_plural = _('URL sites')
  
  def __unicode__(self):
    return self.name + ' (' + self.domain + ')'

class URL(models.Model):
  url = models.CharField(max_length=500, help_text=_('The URI path on the related site.'))
  site = models.ForeignKey(URLSite, help_text=_('The related site for this URL/URI.'))
  
  class Meta:
    verbose_name = _('URL')
    verbose_name_plural = _('URLs')
  
  def __unicode__(self):
    return 'http://%s%s' % (self.site.domain, self.url,)

class Brewer(models.Model):
  slug = AutoSlugField(populate_from='name', unique=True, help_text=_('Slug value for brewer based on the name.'))
  name = models.CharField(max_length=250, help_text=_('Name of the brewer.'))
  
  class Meta:
    ordering = ('name',)
    verbose_name = _('brewer')
    verbose_name_plural = _('brewers')
  
  def __unicode__(self):
    return unicode(self.name)
  
  def get_absolute_url(self):
    return reverse('view_brewer', args=[self.slug])
  
  def get_api_url(self):
    return reverse('beerdb_api_brewer', args=[self.slug])

class Beer(models.Model):
  """
  Beer storage.
  """
  brewer = models.ForeignKey(Brewer, help_text=_('The brewer for this beer.'))
  user = models.ManyToManyField(User, through='UserRating', help_text=_('User ratings for this beer.'))
  url = models.ManyToManyField(URL, help_text=_('External URLs for this beer.'))
  slug = AutoSlugField(populate_from='name', unique_with='brewer', help_text=_('The unique slug for the given beer.'))
  name = models.CharField(max_length=250, help_text=_('The name of the beer.'))
  
  class Meta:
    ordering = ('brewer__name', 'name',)
    verbose_name = _('beer')
    verbose_name_plural = _('beers')
  
  def __unicode__(self):
    return '%s by %s' % (unicode(self.name), unicode(self.brewer.name),)
  
  def get_user_rating(self, username):
    return UserRating.objects.get(beer=self, user__username=username).rating
  
  def get_absolute_url(self):
    return reverse('view_beer', args=[self.brewer.slug, self.slug])
  
  def get_api_url(self):
    return reverse('beerdb_api_beer', args=[self.brewer.slug, self.slug])

class UserRating(models.Model):
  user = models.ForeignKey(User)
  beer = models.ForeignKey(Beer)
  rating = models.ForeignKey(Rating, blank=True, null=True, help_text=_('A rating for this beer by the given user.'))
  note = models.TextField(default='', blank=True, verbose_name='Notes', help_text=_('Notes on this beer by the given user.'))
  date_added = models.DateTimeField(auto_now_add=True, help_text=_('The date on which the user rated the beer.'))
  date_modified = models.DateTimeField(auto_now=True, help_text=_('The last modified date for this rating and/or note.'))
  
  class Meta:
    ordering = ('user', '-date_modified', '-date_added', '-id',)
    verbose_name = _('user beer rating')
    verbose_name_plural = _('user beer ratings')
  
  def __unicode__(self):
    return self.beer.name + ' rating by ' + self.user.username
  
  def get_absolute_url(self):
    return reverse('beerdb_beer_rate', args=[self.beer.brewer.slug, self.beer.slug])