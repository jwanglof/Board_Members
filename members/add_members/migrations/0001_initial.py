# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AddMembers'
        db.create_table('add_members_addmembers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('birthdate', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255, blank=True)),
            ('edu', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('phone_home', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('phone_cell', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('first_liu', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('applied_membership', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('liu_id', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('active_member', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('add_members', ['AddMembers'])


    def backwards(self, orm):
        # Deleting model 'AddMembers'
        db.delete_table('add_members_addmembers')


    models = {
        'add_members.addmembers': {
            'Meta': {'object_name': 'AddMembers'},
            'active_member': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'applied_membership': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'edu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'blank': 'True'}),
            'first_liu': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liu_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_cell': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone_home': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['add_members']