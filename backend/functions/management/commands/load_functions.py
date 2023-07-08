from django.core.management.base import BaseCommand
from functions.models import Function
from users.models import User
import json


class Command(BaseCommand):
    help = " Upload books from a csv file"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str)

    def handle(self, *args, **options):
        json_file = options["json_file"]

        print(json_file)

        with open(json_file, "r") as file:
            reader = json.load(file)

            # print(reader)
            user_admin = User.objects.get(username="admin")
            for row in reader:
                print(row["name"])

                function = Function(
                    name=row["name"], body=row["body"], owner=user_admin
                )

                function.save()

            self.stdout.write(self.style.SUCCESS("json file uploaded"))
