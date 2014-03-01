# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Person.email_addresses'
        db.alter_column(u'mails_person', 'email_addresses', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Person.email_addresses'
        db.alter_column(u'mails_person', 'email_addresses', self.gf('django.db.models.fields.CharField')(max_length=50))

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
            'email_addresses': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['mails']