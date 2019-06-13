from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class post(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Enter a suitable title")
    text = models.TextField(max_length=300, default="Enter the doot here!")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    

