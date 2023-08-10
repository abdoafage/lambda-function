from django.db import models
import uuid
from users.models import User

# Create your models here.


class Function(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    numberOfCalls = models.IntegerField(default=0)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True, default="-")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    runtime = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

    def increase_n_of_call(self):
        self.numberOfCalls += 1
        self.save()
