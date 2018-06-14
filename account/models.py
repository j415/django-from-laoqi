from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    #email = models.EmailField(max_length=20, unique=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)
>>>>>>> add 2.5
