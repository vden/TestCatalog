# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Producer'
        db.create_table('core_producer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('core', ['Producer'])

        # Adding model 'Good'
        db.create_table('core_good', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('producer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Producer'])),
        ))
        db.send_create_signal('core', ['Good'])

        # Adding model 'GoodInfo'
        db.create_table('core_goodinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('good', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Good'])),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Shop'])),
        ))
        db.send_create_signal('core', ['GoodInfo'])

        # Adding model 'Shop'
        db.create_table('core_shop', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('added', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('core', ['Shop'])


    def backwards(self, orm):
        
        # Deleting model 'Producer'
        db.delete_table('core_producer')

        # Deleting model 'Good'
        db.delete_table('core_good')

        # Deleting model 'GoodInfo'
        db.delete_table('core_goodinfo')

        # Deleting model 'Shop'
        db.delete_table('core_shop')


    models = {
        'core.good': {
            'Meta': {'object_name': 'Good'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Producer']"})
        },
        'core.goodinfo': {
            'Meta': {'object_name': 'GoodInfo'},
            'added': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'good': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Good']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Shop']"})
        },
        'core.producer': {
            'Meta': {'object_name': 'Producer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'core.shop': {
            'Meta': {'object_name': 'Shop'},
            'added': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'goods': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Good']", 'through': "orm['core.GoodInfo']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['core']
