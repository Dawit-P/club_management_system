# events/management/commands/populate_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from events.models import Event, News
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with sample data for events and news'

    def handle(self, *args, **options):
        # Create 10 users
        users = []
        for _ in range(10):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()
            user = User.objects.create_user(username=username, email=email, password=password)
            users.append(user)

        # Create 10 events and news
        for _ in range(10):
            title = fake.sentence()
            description = fake.paragraph()
            date = datetime.now() + timedelta(days=random.randint(1, 30))
            author = random.choice(users)

            Event.objects.create(title=title, description=description, date=date, author=author)
            News.objects.create(title=title, description=description, date=date, author=author)

        self.stdout.write(self.style.SUCCESS('Sample data successfully populated.'))
