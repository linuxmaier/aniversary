from django.db import models

# Create your models here.

class Message(models.Model):
	sent_date = models.DateTimeField('date sent')
	subject = models.CharField(max_length=50)
	message = models.TextField()
	full_message = models.TextField()

	def __unicode__(self):
		return self.subject
	
