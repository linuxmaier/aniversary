from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import sys, email, datetime, pytz, re
from mails.models import Message, Person

class Command(BaseCommand):
	option_list = BaseCommand.option_list + (
		make_option('-f',
			'--file',
			action='store_true',
			dest='use_file',
			default=False,
			help='Use specified filed to create email.'),
	)
			
	help = 'Inserts the new emails into the database'
	
	
	def handle(self, *args, **options):

		if options['use_file']:
			msg_file = open(args[0])
		else:
			msg_file = sys.stdin
			if msg_file == '':
				self.stdout.write('Either use -f to specify a file, or input message with stdin.')
				return
		new_msg = email.message_from_file(msg_file)
		
		msg = Message()
		pattern = re.compile('([a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+[a-zA-Z0-9-])')
		person_pattern = re.compile('([A-Za-z]+ [A-Za-z]+)')
		msg.from_address = pattern.search(new_msg.get('from')).group(1)
		try:
			msg.from_person = Person.objects.get(email_addresses__contains=msg.from_address)
		except Person.DoesNotExist:
			new_person_name = person_pattern.search(new_msg.get('from')).group(1).split(' ')
			new_person = Person(first_name=new_person_name[0], last_name=new_person_name[1], email_addresses=msg.from_address)
			new_person.save()
			msg.from_person = new_person
		msg.to_address = pattern.search(new_msg.get('to')).group(1)
		try:
			msg.to_person = Person.objects.get(email_addresses__contains=msg.to_address)
		except Person.DoesNotExist:
			new_person_name = person_pattern.search(new_msg.get('to')).group(1).split(' ')
			new_person = Person(first_name=new_person_name[0], last_name=new_person_name[1], email_addresses=msg.to_address)
			new_person.save()
			msg.to_person = new_person
		
		msg_date = new_msg.get('date')
		msg_date = datetime.datetime.strptime(msg_date[:-6], '%a, %d %b %Y %H:%M:%S')
		msg_tz = pytz.timezone('America/Chicago')
		msg_date = msg_tz.localize(msg_date)
		msg_date = msg_date.astimezone(pytz.utc)
		msg.sent_date = msg_date
		
		msg.subject = new_msg.get('subject')
		msg.message = new_msg.get_payload()
		msg.full_message = new_msg.as_string()
		msg.save()
		
