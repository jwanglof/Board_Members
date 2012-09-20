# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SeeMembers.first_liu'
        db.delete_column('see_members_seemembers', 'first_liu')

        # Deleting field 'SeeMembers.town'
        db.delete_column('see_members_seemembers', 'town')

        # Deleting field 'SeeMembers.surname'
        db.delete_column('see_members_seemembers', 'surname')

        # Deleting field 'SeeMembers.firstname'
        db.delete_column('see_members_seemembers', 'firstname')

        # Deleting field 'SeeMembers.phone_home'
        db.delete_column('see_members_seemembers', 'phone_home')

        # Deleting field 'SeeMembers.notes'
        db.delete_column('see_members_seemembers', 'notes')

        # Deleting field 'SeeMembers.edu'
        db.delete_column('see_members_seemembers', 'edu')

        # Deleting field 'SeeMembers.birthdate'
        db.delete_column('see_members_seemembers', 'birthdate')

        # Deleting field 'SeeMembers.phone_cell'
        db.delete_column('see_members_seemembers', 'phone_cell')

        # Deleting field 'SeeMembers.active_member'
        db.delete_column('see_members_seemembers', 'active_member')

        # Deleting field 'SeeMembers.applied_membership'
        db.delete_column('see_members_seemembers', 'applied_membership')

        # Deleting field 'SeeMembers.address'
        db.delete_column('see_members_seemembers', 'address')

        # Deleting field 'SeeMembers.liu_id'
        db.delete_column('see_members_seemembers', 'liu_id')

        # Deleting field 'SeeMembers.email'
        db.delete_column('see_members_seemembers', 'email')

        # Deleting field 'SeeMembers.zip_code'
        db.delete_column('see_members_seemembers', 'zip_code')


    def backwards(self, orm):
        # Adding field 'SeeMembers.first_liu'
        db.add_column('see_members_seemembers', 'first_liu',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'SeeMembers.town'
        db.add_column('see_members_seemembers', 'town',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'SeeMembers.surname'
        db.add_column('see_members_seemembers', 'surname',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255),
                      keep_default=False)

        # Adding field 'SeeMembers.firstname'
        db.add_column('see_members_seemembers', 'firstname',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255),
                      keep_default=False)

        # Adding field 'SeeMembers.phone_home'
        db.add_column('see_members_seemembers', 'phone_home',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SeeMembers.notes'
        db.add_column('see_members_seemembers', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SeeMembers.edu'
        db.add_column('see_members_seemembers', 'edu',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'SeeMembers.birthdate'
        db.add_column('see_members_seemembers', 'birthdate',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SeeMembers.phone_cell'
        db.add_column('see_members_seemembers', 'phone_cell',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SeeMembers.active_member'
        db.add_column('see_members_seemembers', 'active_member',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SeeMembers.applied_membership'
        db.add_column('see_members_seemembers', 'applied_membership',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'SeeMembers.address'
        db.add_column('see_members_seemembers', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'SeeMembers.liu_id'
        db.add_column('see_members_seemembers', 'liu_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'SeeMembers.email'
        db.add_column('see_members_seemembers', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'SeeMembers.zip_code'
        db.add_column('see_members_seemembers', 'zip_code',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    models = {
        'see_members.seemembers': {
            'Meta': {'object_name': 'SeeMembers'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['see_members']