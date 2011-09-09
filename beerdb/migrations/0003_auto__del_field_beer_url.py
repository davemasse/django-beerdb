# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Beer.url'
        db.delete_column('beerdb_beer', 'url_id')

        # Adding M2M table for field url on 'Beer'
        db.create_table('beerdb_beer_url', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('beer', models.ForeignKey(orm['beerdb.beer'], null=False)),
            ('url', models.ForeignKey(orm['beerdb.url'], null=False))
        ))
        db.create_unique('beerdb_beer_url', ['beer_id', 'url_id'])


    def backwards(self, orm):
        
        # Adding field 'Beer.url'
        db.add_column('beerdb_beer', 'url', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beerdb.URL'], null=True, blank=True), keep_default=False)

        # Removing M2M table for field url on 'Beer'
        db.delete_table('beerdb_beer_url')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'beerdb.beer': {
            'Meta': {'ordering': "('brewer__name', 'name')", 'object_name': 'Beer'},
            'brewer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beerdb.Brewer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'url': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['beerdb.URL']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['beerdb.UserBeer']", 'symmetrical': 'False'})
        },
        'beerdb.brewer': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Brewer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'})
        },
        'beerdb.rating': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Rating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'default': "''", 'unique': 'True', 'populate_from': 'None', 'db_index': 'True'})
        },
        'beerdb.url': {
            'Meta': {'object_name': 'URL'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beerdb.URLSite']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'beerdb.urlsite': {
            'Meta': {'object_name': 'URLSite'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'beerdb.userbeer': {
            'Meta': {'ordering': "('-date_modified', '-date_added', '-id')", 'object_name': 'UserBeer'},
            'beer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beerdb.Beer']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'rating': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beerdb.Rating']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['beerdb']
