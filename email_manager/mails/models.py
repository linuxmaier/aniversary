from django.db import models

# Create your models here.

#class Person(models.Model):
#	full_name = models.CharField(max_length=20)
#	first_name = models.CharField(max_length=20)
#	last_name = models.CharField(max_length=20)

class Message(models.Model):
	from_address = models.EmailField()
#	from_person = models.ForeignKey(Person)
	to_address = models.EmailField()
#	to_person = models.ForeignKey(Person)
	sent_date = models.DateTimeField('date sent')
	subject = models.CharField(max_length=50)
	message = models.TextField()
	full_message = models.TextField()

	def __unicode__(self):
		return self.subject
	
	
