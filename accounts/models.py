from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser )
# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, default="abc123@xyz.com")
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email