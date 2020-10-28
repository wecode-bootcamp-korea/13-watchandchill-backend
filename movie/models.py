from django.db import models

class Movies(models.Model):
	title		 = models.CharField(max_length=100)
	premier_date = models.DateField(max_length=100)
	country		 = models.CharField(max_length=100)
	run_time	 = models.CharField(max_length=10)
	poster_url	 = models.URLField(max_length=1000)
	in_theaters  = models.BooleanField()
	service		 = models.ManyToManyField('Services', through='MovieServices', related_name='services')
	genre		 = models.ManyToManyField('Genres', through='MovieGenres', related_name='genres')
	tag 		 = models.ManyToManyField('Tags', through='MovieTags', related_name='tags')
	casting		 = models.ManyToManyField('People', through='Cast', related_name='people')
	description	 = models.CharField(max_length=1000)
	coverpic_url = models.URLField(max_length=200)

	class Meta:
		db_table= 'movies'


class MoviePhotos(models.Model) :
	photo_url	= models.URLField(max_length=200)
	movie		= models.ForeignKey('Movies', on_delete=models.CASCADE)
	class Meta:
		db_table= 'photos'


class MovieVideos(models.Model) :
	video_url	= models.URLField(max_length=200)
	movie		= models.ForeignKey('Movies', on_delete=models.CASCADE)
	class Meta:
		db_table= 'videos'


class Cast(models.Model) :
	name		= models.ForeignKey('People', on_delete=models.CASCADE)
	role		= models.CharField(max_length=5000)
	cast_as		= models.CharField(max_length=50)
	movie		= models.ForeignKey('Movies', on_delete=models.CASCADE)
	class Meta:
		db_table='cast'


class People(models.Model) :
	name		= models.CharField(max_length=100)
	avatar_url	= models.CharField(max_length=200, null=True)	
	class Meta:
		db_table='people'


class Genres(models.Model) :
	name		= models.CharField(max_length=100)
	class Meta:
		db_table='genres'


class MovieGenres(models.Model) :
	movie		= models.ForeignKey('Movies', on_delete=models.CASCADE)
	genres		= models.ForeignKey('Genres', on_delete=models.CASCADE)
	class Meta:
		db_table='movie_genres'


class Tags(models.Model) :
	name		= models.CharField(max_length=50)
	class Meta:
		db_table='tags'


class MovieTags(models.Model) :
	tag 		= models.ForeignKey('Tags', on_delete=models.CASCADE)
	movie		= models.ForeignKey('Movies', on_delete=models.CASCADE)
	class Meta:
		db_table='movie_tags'


class Services(models.Model) :
	name		= models.CharField(max_length=50)
	icon_url	= models.CharField(max_length=2000, null=True)
	class Meta:
		db_table='services'


class MovieServices(models.Model) :
	service 	=models.ForeignKey('Services', on_delete=models.CASCADE)
	movie 		=models.ForeignKey('Movies', on_delete=models.CASCADE)
	class Meta:
		db_table='movie_services'