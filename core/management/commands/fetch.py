from django.core.management.base import BaseCommand
from django.utils import timezone

def show_time():
	time = timezone.now().strftime('%X')
    self.stdout.write("It's now %s" % time)

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
    	show_time()
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)