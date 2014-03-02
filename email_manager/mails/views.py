from django.shortcuts import render
from django.http import HttpResponse
from mails.models import Person, Message
import datetime, random, pytz


# Create your views here.

def index(request):
	new_msgs = get_new_messages(365)
	new_msg = new_msgs[int(random.random() * new_msgs.count())]
	delta_to_old = datetime.datetime.now(tz=pytz.utc) - new_msg.sent_date
	old_msgs = get_old_messages(delta_to_old.days + 365)
	old_msg = old_msgs[int(random.random() * old_msgs.count())]
	delta_msgs = new_msg.sent_date - old_msg.sent_date
	context = {'old_msg': old_msg, 'new_msg': new_msg, 'delta': delta_msgs}
	return render(request, 'mails/lovenote.html', context)

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

def get_new_messages(days_ago):
	return Message.objects.filter(sent_date__gte=datetime.datetime.now(tz=pytz.utc) - datetime.timedelta(days=days_ago))

def get_old_messages(days_ago):
	return Message.objects.filter(sent_date__lte=datetime.datetime.now(tz=pytz.utc) - datetime.timedelta(days=days_ago))
