from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import sys, email, datetime, pytz
from mails.models import Message

class Command(BaseCommand):
	option_list = BaseCommand.option_list + (
		make_option('-f',
			'--file',
			action='store_true',
			dest='use_file',
			default=False,
			help='Use specified filed to create email.'),
#		make_option('-s',
#			'--stdin',
#			action='store_false',
#			dest='use_file',
#			default=False,
#			help='Use stdin to import mail.'),
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
		