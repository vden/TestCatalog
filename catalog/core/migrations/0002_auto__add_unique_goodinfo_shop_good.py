# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'GoodInfo', fields ['shop', 'good']
        db.create_unique('core_goodinfo', ['shop_id', 'good_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'GoodInfo', fields ['shop', 'good']
        db.delete_unique('core_goodinfo', ['shop_id', 'good_id'])


    models = {
        'core.good': {
            'Meta': {'object_name': 'Good'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Producer']"})
        },
        'core.goodinfo': {
            'Meta': {'unique_together': "(('good', 'shop'),)", 'object_name': 'GoodInfo'},
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
