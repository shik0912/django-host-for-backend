import subprocess
from django.core.management.base import BaseCommand

def execute(projectname):
        subprocess.call(
            "cd .. && django-admin.py startproject " + projectname, 
            shell=True
        )

class Command(BaseCommand):
    help = 'IT IS CUSTOM'
    args = '[projectname ...]'

    def add_arguments(self, parser):
        parser.add_argument(
            dest='projectname',
            help='the name to process',
        )
    
    def handle(self, *args, **options):
        projectname = options['projectname']
        execute(projectname)