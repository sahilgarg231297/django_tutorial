import os
import django
import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")
django.setup()

# FAKE POP SCRIPT

fakegen = Faker()
topics = ["Search", "Marketplace", "News", "Games"]


def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=4):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[
            0
        ]

        access_record = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[
            0
        ]


if __name__ == "__main__":
    print("Populating scripts!")
    populate(30)
    print("Populating completed!")
