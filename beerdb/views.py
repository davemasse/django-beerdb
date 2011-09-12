from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, DetailView, FormView, ListView

from beerdb.forms import UserRatingForm
from beerdb.models import Beer, Brewer, UserRating

# Generic views

class BeerDetailView(DetailView):
  context_object_name = 'beer'
  model = Beer
  
  def get_context_data(self, **kwargs):
    context = super(BeerDetailView, self).get_context_data(**kwargs)
    
    try:
      user_rating = UserRating.objects.get(user=self.request.user, beer=context['object'])
    except UserRating.DoesNotExist:
      user_rating = UserRating.objects.none()
    
    context.update({
      'user_rating': user_rating,
      'other_user_ratings': context['object'].userrating_set.exclude(user__is_staff=True)
    })
    
    return context

class BeerListView(ListView):
  context_object_name = 'beers'
  model = Beer

class BrewerDetailView(DetailView):
  context_object_name = 'brewer'
  model = Brewer

class BrewerListView(ListView):
  context_object_name = 'brewers'
  model = Brewer

class UserDetailView(DetailView):
  context_object_name = 'user'
  model = User
  # Exclude site staff
  queryset = User.objects.exclude(is_staff=True)
  # Select user by username
  slug_field = 'username'

# Custom views

@login_required
def beer_rate(request, brewer_slug, beer_slug):
  try:
    beer = Beer.objects.get(brewer__slug=brewer_slug, slug=beer_slug)
  except Beer.DoesNotExist:
    raise Http404
  
  try:
    user_rating = UserRating.objects.get(user=request.user, beer=beer)
  except UserRating.DoesNotExist:
    user_rating = UserRating(user=request.user, beer=beer)
  
  if request.method == 'POST':
    user_rating_form = UserRatingForm(request.POST, instance=user_rating)
    
    if user_rating_form.is_valid():
      user_rating_form.cleaned_data['beer'] = beer
      user_rating_form.cleaned_data['user'] = request.user
      
      user_rating = user_rating_form.save()
      
      messages.success(request, _('Your rating was successfully saved.'))
      
      return HttpResponseRedirect(reverse('beerdb_beer_detail', args=[beer.brewer.slug, beer.slug]))
  else:
    user_rating_form = UserRatingForm(instance=user_rating)
  
  return render_to_response('beerdb/beer_rate.html',
    {
      'beer': beer,
      'user_rating_form': user_rating_form,
    }, context_instance=RequestContext(request))