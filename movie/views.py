#Python
import json
#Django
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
#Custom
from movie.models import Movies, MoviePhotos, MovieVideos, Cast, People, Genres, MovieGenres, Tags, MovieTags, Services, MovieServices


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
			} for movie in theater_library[:20]]


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
			movie 	 	= Movies.objects.get(id = movie_id)
			photos 		= MoviePhotos.objects.filter(id = movie_id)
			videos 		= MovieVideos.objects.filter(id = movie_id)
			cast_list 	= Cast.objects.filter(movie = movie_id)
			actor_name 	= [People.objects.get(id =person).name for person in cast_list.values_list('name', flat=True)]
			cast_as 	= [person.cast_as for person in cast_list.all()]
			cast 		= [{'name': person.name.name, 'role': person.role, 'cast_as': person.cast_as, 'photo': person.name.avatar_url} for person in Cast.objects.filter(movie = movie_id)]
			all_info 	={
				'id'			: movie_id,
				'title'			: movie.title,
				'date'			: movie.premier_date,
				'poster_url'	: movie.poster_url,
				'country'		: movie.country,
				'service'		: list(movie.service.values_list('name', flat=True)),
				'genre'			: list(movie.genre.values_list('name', flat=True)),
				'photos'		: list(MoviePhotos.objects.values_list('photo_url', flat=True)),
				'videos'		: list(MovieVideos.objects.values_list('video_url', flat=True)),
				'tag'			: list(movie.genre.values_list('name', flat=True)),
				'runtime'		: movie.run_time,
				'description'	: movie.description,
				'cast'			: list(cast)
			}
			return JsonResponse ({'movie information': all_info}, status=200)
		except Movies.DoesNotExist:
			return JsonResponse ({'KeyError': 'Non-existant movie id'})
