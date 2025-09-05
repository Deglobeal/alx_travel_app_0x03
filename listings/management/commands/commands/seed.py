from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **kwargs):
        # Create a default user if none exists
        if not User.objects.exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
            self.stdout.write(self.style.SUCCESS('Created default user "admin"'))
        
        user = User.objects.first()
        locations = ["New York", "Paris", "Tokyo", "London", "Berlin"]
        listings_data = [
            {
                "title": f"Listing {i}",
                "description": f"Beautiful property in {locations[i % len(locations)]}",
                "price": round(random.uniform(50, 300), 2),
                "location": locations[i % len(locations)]
            } for i in range(1, 11)
        ]

        created_count = 0
        for data in listings_data:
            _, created = Listing.objects.get_or_create(
                owner=user,
                defaults=data
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {created_count} listings'))