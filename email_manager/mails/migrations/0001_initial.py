# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'mails_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email_addresses', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'mails', ['Person'])

        # Adding model 'Message'
        db.create_table(u'mails_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('from_person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sent_mail', to=orm['mails.Person'])),
            ('to_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('to_person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='received_mail', to=orm['mails.Person'])),
            ('sent_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('full_message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'mails', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'mails_person')

        # Deleting model 'Message'
        db.delete_table(u'mails_message')


    models = {
        u'mails.message': {
            'Meta': {'object_name': 'Message'},
            'from_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'from_person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_mail'", 'to': u"orm['mails.Person']"}),
            'full_message': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'sent_date': ('django.db.models.fields.DateTimeField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'to_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'to_person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'received_mail'", 'to': u"orm['mails.Person']"})
        },
        u'mails.person': {
            'Meta': {'object_name': 'Person'},
            'email_addresses': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['mails']