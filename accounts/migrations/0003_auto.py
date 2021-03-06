# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding M2M table for field peers on 'UserProfile'
        db.create_table('accounts_userprofile_peers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['accounts.userprofile'], null=False)),
            ('peer', models.ForeignKey(orm['peers.peer'], null=False))
        ))
        db.create_unique('accounts_userprofile_peers', ['userprofile_id', 'peer_id'])
    
    
    def backwards(self, orm):
        
        # Removing M2M table for field peers on 'UserProfile'
        db.delete_table('accounts_userprofile_peers')
    
    
    models = {
        'accounts.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'peer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['peers.Peer']"}),
            'peers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'peer_info'", 'symmetrical': 'False', 'to': "orm['peers.Peer']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 9, 28, 11, 12, 34, 315403)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 9, 28, 11, 12, 34, 315358)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'peers.peer': {
            'Meta': {'object_name': 'Peer', 'db_table': "u'peer'"},
            'domain_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'networks': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['peers.PeerRange']", 'null': 'True', 'blank': 'True'}),
            'peer_as': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'peer_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'peer_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'peer_tag': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'techc_emails': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['peers.TechcEmail']", 'null': 'True', 'blank': 'True'})
        },
        'peers.peerrange': {
            'Meta': {'object_name': 'PeerRange', 'db_table': "u'peer_range'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'peers.techcemail': {
            'Meta': {'object_name': 'TechcEmail', 'db_table': "'techc_email'"},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '352', 'db_column': "'email'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['accounts']
