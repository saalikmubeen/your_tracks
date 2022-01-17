from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.


class Track(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
