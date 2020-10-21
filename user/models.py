from django.db import models


class User(models.Model):
    email             = models.CharField(max_length=200)
    name              = models.CharField(max_length=50)
    password          = models.CharField(max_length=300)
    profile_image_url = models.CharField(max_length=2000)

    class Meta :
        db_table = 'users'


"""
class UserStatus(models.Model):
    user            = models.ForeignKey('User', on_delete=models.CASCADE)
    movie           = models.ForeignKey('Movie', on_delete=models.CASCADE)
    status          = models.ForeignKey('StatusType', on_delete=models.CASCADE)

    class Meta :
        db_table = 'user_status'


class StatusType(models.Model):
    status = models.CharField(max_length=50)

    class Meta :
        db_table = 'status_types'

"""


