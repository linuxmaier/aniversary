from django.shortcuts import render
from django.http import HttpResponse
from mails.models import Person, Message
import datetime, random, pytz


# Create your views here.

def index(request):
	response = HttpResponse()
	response.write(old(request))
	response.write(new(request))

	return response

def old(request):
	old_msgs = Message.objects.filter(sent_date__lte=datetime.datetime.now(tz=pytz.utc) - datetime.timedelta(days=365))
	msg = old_msgs[int(random.random() * old_msgs.count())]
	context = {'msg': msg}
	return render(request, 'mails/index.html', context)
	
def new(request):
	new_msgs = Message.objects.filter(sent_date__gte=datetime.datetime.now(tz=pytz.utc) - datetime.timedelta(days=365))
	msg = new_msgs[int(random.random() * new_msgs.count())]
	context = {'msg': msg}
	return render(request, 'mails/index.html', context)
