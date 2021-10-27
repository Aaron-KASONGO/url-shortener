from django.db import models
from django.contrib.auth.models import User
import string
import random


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    update_date = models.DateTimeField(auto_now=True)


class MiniUrl(models.Model):
    url = models.URLField(unique=True)
    code = models.CharField(max_length=30, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    pseudo = models.CharField(max_length=30, blank=True, null=True)
    nb_access = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

    """def save(self, *args, **kwargs):
        if not self.pk:
            self.generate(6)

        super(MiniUrl, self).save(*args, **kwargs)

    def generate(self, nb):
        caracters = string.ascii_letters + string.digits
        code_list = [random.choice(caracters) for _ in range(nb)]
        code = ''.join(code_list)
        
        while self.objects.filter(code=code).exists():
            code_list = [random.choice(caracters) for _ in range(nb)]
            code = ''.join(code_list)

        self.code = code"""
