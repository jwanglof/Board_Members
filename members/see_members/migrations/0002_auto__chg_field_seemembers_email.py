# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SeeMembers.email'
        db.alter_column('see_members_seemembers', 'email', self.gf('django.db.models.fields.EmailField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'SeeMembers.email'
        db.alter_column('see_members_seemembers', 'email', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        'see_members.seemembers': {
            'Meta': {'object_name': 'SeeMembers'},
            'active_member': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'applied_membership': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '12', 'blank': 'True'}),
            'edu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'blank': 'True'}),
            'first_liu': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liu_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_cell': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '11', 'blank': 'True'}),
            'phone_home': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '6', 'blank': 'True'})
        }
    }

    complete_apps = ['see_members']