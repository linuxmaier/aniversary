# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.html_message'
        db.add_column(u'mails_message', 'html_message',
                      self.gf('django.db.models.fields.TextField')(default='insert html here'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Message.html_message'
        db.delete_column(u'mails_message', 'html_message')


    models = {
        u'mails.message': {
            'Meta': {'object_name': 'Message'},
            'from_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'from_person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_mail'", 'to': u"orm['mails.Person']"}),
            'full_message': ('django.db.models.fields.TextField', [], {'default': "'full message including headers'"}),
            'html_message': ('django.db.models.fields.TextField', [], {'default': "'insert html here'"}),
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