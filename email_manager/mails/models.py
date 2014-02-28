from django.db import models

# Create your models here.

class Person(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email_addresses = models.CharField(max_length=50)

	def __unicode__(self):
		return first_name + last_name

class Message(models.Model):
	from_address = models.EmailField()
	from_person = models.ForeignKey(Person, related_name='sent_mail')
	to_address = models.EmailField()
	to_person = models.ForeignKey(Person, related_name='received_mail')
	sent_date = models.DateTimeField('date sent')
	subject = models.CharField(max_length=50)
	message = models.TextField()
	full_message = models.TextField()

	def __unicode__(self):
		return self.subject
	
	
