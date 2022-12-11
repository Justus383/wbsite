from django.db import models
from django.db import models
from django.contrib.auth.models import User


class ProfileData(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    excelid = models.IntegerField(User, null=True)

    def __str__(self):
        return str(self.user)