#Python
import json
#Django
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
#Custom
from movie.models import *


class ListView(View):
	def get(self, request) :
		library = Movies.objects.all()

#IN THEATERS
		theater_library	= library.filter(in_theaters = '1')
		theater_movies	= [{
			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()],
			'genre'	 : list(movie.genre.values_list('name', flat= True))
			} for movie in theater_library[0:20]]


#WATCHA ROW
		watcha_library	= library.filter(service = '2')
		watcha_movies	= [{
			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()],
			'genre'	 : list(movie.genre.values_list('name', flat= True))
			} for movie in watcha_library[0:20]]
# NETFLIX ROW
		netflix_library	= library.filter(service = '1')
		netflix_movies	= [{
			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()],
			'genre'	 : list(movie.genre.values_list('name', flat= True))
			} for movie in netflix_library[0:20]]
# KOREA-BEST ROW
		korean_library	= library.filter(country = '한국')
		korean_movies	= [{
 			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()],
			'genre'	 : list(movie.genre.values_list('name', flat= True))
			} for movie in korean_library[0:20]]
# US-BEST ROW
		us_library		= library.filter(country = '미국')
		us_movies		= [{
 			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()],
			'genre'	 : list(movie.genre.values_list('name', flat= True))
			} for movie in us_library[0:20]]
# ACTION ROW
		action_library	= library.filter(genre = '2')
		action_movies 	= [{
 			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()],
			'genre'	 : list(movie.genre.values_list('name', flat= True))
			} for movie in action_library[0:20]]
# COMEDY ROW
		comedy_library 	= library.filter(genre = '12')
		comedy_movies 	= [{
 			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()],
			'genre'	 : list(movie.genre.values_list('name', flat= True))
			} for movie in comedy_library[0:20]]
		return JsonResponse ({
							'theater'	: theater_movies,
							'watcha' 	: watcha_movies,
							'netflix'	: netflix_movies, 
							'kr'		: korean_movies,
							'us'		: us_movies,
							'action'	: action_movies,
							'comedy'	: comedy_movies,
							}, status=200)


class PageView(View) :
	def get(self, request, movie_id) :
		try:
			data 	 	= json.loads(request.body)
			movie_info 	= Movies.objects.get(id = movie_id)
			photos 		= MoviePhotos.objects.filter(id = movie_id)
			videos 		= MovieVideos.objects.filter(id = movie_id)
			cast_list 	= Cast.objects.filter(movie = movie_id)
			actor_id 	= cast_list.all().values_list('id', flat=True)
			actor_name 	= [People.objects.get(id =person).name for person in cast_list.all().values_list('name', flat=True)]
			actor_photo	= [People.objects.get(id =person).avatar_url for person in cast_list.all().values_list('name', flat=True)]
			role_type 	= [person.role for person in cast_list.all()]
			cast_as 	= [person.cast_as for person in cast_list.all()]
			cast_bank	= [{'name': actor_name[i], 'role': role_type[i], 'cast_as': cast_as[i], 'photo': actor_photo[i]} for i in range(1,12)]
			all_info 	={
				'id'			: movie_info.id,
				'title'			: movie_info.title,
				'date'			: movie_info.premier_date,
				'poster_url'	: movie_info.poster_url,
				'country'		: movie_info.country,
				'service'		: list(movie_info.service.values_list('name', flat=True)),
				'genre'			: list(movie_info.genre.values_list('name', flat=True)),
				'photos'		: list(photos.values_list('photo_url', flat=True)),
				'videos'		: list(videos.values_list('video_url', flat=True)),
				'tag'			: list(movie_info.genre.values_list('name', flat=True)),
				'runtime'		: movie_info.run_time,
				'premier'		: movie_info.premier_date,
				'cast'			: cast_bank
			}
			return JsonResponse ({'movie information': all_info}, status=200)
		except Movies.DoesNotExist:
			return JsonResponse ({'KeyError': 'Non-existant movie id'})
