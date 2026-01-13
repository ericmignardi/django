from django.core.management.base import BaseCommand
from api.models import GrainPrice
from decimal import Decimal


class Command(BaseCommand):
    help = 'Seeds the database with sample grain prices'

    def handle(self, *args, **options):
        # Sample grain data
        grains = [
            {'grain_type': 'Wheat', 'price': Decimal('7.25')},
            {'grain_type': 'Corn', 'price': Decimal('5.85')},
            {'grain_type': 'Soybeans', 'price': Decimal('13.50')},
            {'grain_type': 'Oats', 'price': Decimal('3.95')},
            {'grain_type': 'Barley', 'price': Decimal('6.10')},
            {'grain_type': 'Rice', 'price': Decimal('15.75')},
            {'grain_type': 'Sorghum', 'price': Decimal('5.40')},
            {'grain_type': 'Rye', 'price': Decimal('4.80')},
        ]

        # Only seed if no prices exist
        if GrainPrice.objects.exists():
            self.stdout.write(self.style.WARNING('Grain prices already exist. Skipping seed.'))
            return

        for grain in grains:
            GrainPrice.objects.create(**grain)
            self.stdout.write(f"Created {grain['grain_type']} at ${grain['price']}")

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(grains)} grain prices'))
