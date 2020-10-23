from django.db import models


class User(models.Model):
    email             = models.CharField(max_length=200)
    name              = models.CharField(max_length=50)
    password          = models.CharField(max_length=300)
    profile_image_url = models.CharField(max_length=2000)

    class Meta :
        db_table = 'users'

