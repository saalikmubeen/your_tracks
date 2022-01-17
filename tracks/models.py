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
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Like(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    liked_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    track = models.ForeignKey(
        Track, on_delete=models.CASCADE, related_name="likes")
    
    class Meta:
        unique_together = ('liked_by', 'track',)
        
    def __str__(self):
        return f'{self.liked_by} likes {self.track}'