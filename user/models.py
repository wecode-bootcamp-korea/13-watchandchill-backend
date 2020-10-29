from django.db import models
from movie.models import Movies


class User(models.Model):
    email             = models.CharField(max_length=200)
    name              = models.CharField(max_length=50)
    password          = models.CharField(max_length=300)
    profile_image_url = models.CharField(max_length=2000)
    MovieStatus 	  = models.ManyToManyField('Status', through = 'UserStatus', related_name= 'status' )

    class Meta :
        db_table = 'users'

class Status(models.Model):
	name	= models.CharField(max_length=100)

	class Meta :
		db_table = 'status'

class UserStatus(models.Model):
	user 	= models.ForeignKey('User', on_delete = models.CASCADE)
	movie 	= models.ForeignKey('movie.Movies', on_delete = models.CASCADE)
	status 	= models.ForeignKey('status', on_delete = models.CASCADE)