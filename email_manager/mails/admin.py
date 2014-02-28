from django.contrib import admin
from mails.models import Message, Person

# Register your models here.

admin.site.register(Person)
admin.site.register(Message)
