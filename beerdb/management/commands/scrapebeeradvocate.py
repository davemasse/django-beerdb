import re
import sys
from optparse import make_option
from pyquery import PyQuery

from django.core.management.base import BaseCommand, CommandError

from beerdb.models import Beer, Brewer, URL, URLSite

DOMAIN = 'beeradvocate.com'

class Command(BaseCommand):
  option_list = BaseCommand.option_list + (
    make_option('--brewerids', '-b', dest='brewer_ids', type='str', help='The brewer ID to use for scraping'),
  )
  help = ''
  
  def get_brewer(self, brewer_id):
    url = 'http://beeradvocate.com/beer/profile/%s/?view=beers&show=all' % (brewer_id,)
    
    self.p = PyQuery(url=url)
    
    brewer_name = self.p('h1').text()
    
    if re.search('^404 Not Found', brewer_name):
      print >> sys.stderr, 'Brewer not found'
      return
    
    print 'Brewer: ' + brewer_name.encode('ascii', 'ignore')
    
    try:
      brewer = Brewer.objects.get(name=brewer_name)
    except Brewer.DoesNotExist:
      brewer = Brewer.objects.create(name=brewer_name)
    
    # Iterate over all beer links
    for tag in self.p('a[href^="/beer/profile/"]'):
      # Look for matching profile link
      if re.search('^/beer/profile/\d+/\d+$', self.p(tag).attr('href')):
        s = re.search('^/beer/profile/\d+/(\d+)$', self.p(tag).attr('href'))
        
        # Select beer ID value from link
        beer_id = s.group(1)
        
        # Create the beer record
        self.get_beer(brewer, beer_id, tag)
  
  def get_beer(self, brewer, beer_id, tag):
    try:
      # Get beer name
      beer_name = self.p(tag).find('b').text()
      
      # Ignore empty names
      if len(beer_name) == 0:
        raise Exception('Name failure')
    except:
      return
    
    try:
      # Find an existing matching record
      beer = Beer.objects.get(name=beer_name, brewer=brewer)
    except Beer.DoesNotExist:
      # Create a new URL record for the beer
      url = URL.objects.create(url=self.p(tag).attr('href'), site=self.url_site)
      
      # Create the beer record
      beer = Beer.objects.create(brewer=brewer, name=beer_name)
      # Connect the URL record
      beer.url.add(url)
      beer.save()
      
      try:
        # Display the beer name for debugging purposes
        print beer_name.encode('ascii', 'ignore')
      except:
        print "[!!] Can't display beer name."
  
  def handle(self, **options):
    if 'brewer_ids' not in options:
      print >> sys.stderr, 'At least one brewer ID is required'
      sys.exit(1)
    
    brewer_ids = options['brewer_ids']
    
    self.url_site = URLSite.objects.get(domain=DOMAIN)
    
    ids = []
    # Split up brewer ID string
    for id in brewer_ids.split(','):
      if '-' in id:
        id_range = id.split('-')
        min = int(id_range[0])
        max = int(id_range[1]) + 1
        for i in range(min, max):
          ids.append(i)
      else:
        ids.append(int(id))
    
    # Iterate through requested brewer IDs
    for id in ids:
      self.get_brewer(id)
    
    '''
    # Iterate through listing of breweries
    
    # Breweries
    pages = range(0, 4000, 20)
    
    for page_id in pages:
      # Breweries
      url = 'http://beeradvocate.com/beerfly/list.php?start=%d&name=%%25&brewery=Y&sort=name' % (page_id,)
      
      p = PyQuery(url=url)
      
      for tag in p('a[href="^=/beer/profile/"]'):
        if re.search('^/beer/profile/(\d+)/?', p(tag).attr('href')):
          s = re.search('^/beer/profile/(\d+)/?', p(tag).attr('href'))
          
          brewer_id = s.group(1)
    '''