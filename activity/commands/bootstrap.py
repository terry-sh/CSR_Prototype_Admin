from django.core.management.base import BaseCommand
from ..models.language import Language
from ..models.unit import Unit

class Command(BaseCommand):
    help = 'Bootstrapping application'

    def handle(self, *args, **options):
        pass
        # Initialize data etc.
        # Unit.objects.create(name='Kilogram', abbr='kg')