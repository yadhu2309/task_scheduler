from typing import Any
from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime, timedelta
fake = Faker()

from tasks.models import Tasks
from userapp.models import User

class Command(BaseCommand):
    help = "Command to create tasks"

    def handle(self, *args: Any, **options: Any) -> str | None:
        user = User.objects.get(email='yadhu@gmail.com')
        for _ in range(5):
            tasks = Tasks.objects.create(user=user,
                          title=fake.name(), 
                          # description=fake.text(),
                        #   created_at=datetime.now(),
                          date=datetime.now().date(),
                          start=datetime.now().time().replace(microsecond=0),
                          end=(datetime.now()+timedelta(hours=1)).time().replace(microsecond=0)
                          )
        self.stdout.write(self.style.SUCCESS('Command finished'))

    