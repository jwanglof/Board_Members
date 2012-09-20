# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SeeMembers.birthdate'
        db.alter_column('see_members_seemembers', 'birthdate', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'SeeMembers.phone_cell'
        db.alter_column('see_members_seemembers', 'phone_cell', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'SeeMembers.phone_home'
        db.alter_column('see_members_seemembers', 'phone_home', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'SeeMembers.zip_code'
        db.alter_column('see_members_seemembers', 'zip_code', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'SeeMembers.birthdate'
        db.alter_column('see_members_seemembers', 'birthdate', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'SeeMembers.phone_cell'
        db.alter_column('see_members_seemembers', 'phone_cell', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'SeeMembers.phone_home'
        db.alter_column('see_members_seemembers', 'phone_home', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'SeeMembers.zip_code'
        db.alter_column('see_members_seemembers', 'zip_code', self.gf('django.db.models.fields.PositiveIntegerField')())

    models = {
        'see_members.seemembers': {
            'Meta': {'object_name': 'SeeMembers'},
            'active_member': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'applied_membership': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'edu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'blank': 'True'}),
            'first_liu': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liu_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_cell': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'phone_home': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['see_members']