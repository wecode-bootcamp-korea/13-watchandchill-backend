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
			'service': [service.name for service in movie.service.all()]
			} for movie in theater_library]
#WATCHA ROW
		watcha_library	= library.filter(service = '2')
		watcha_movies	= [{
 			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()]
			} for movie in watcha_library]
# NETFLIX ROW
		netflix_library	= library.filter(service = '1')
		netflix_movies	= [{
 			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()]
			} for movie in netflix_library]
# KOREA-BEST ROW
		korean_library	= library.filter(country = '한국')
		korean_movies	= [{
 			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()]
			} for movie in korean_library]
# US-BEST ROW
		us_library		= library.filter(country = '미국')
		us_movies		= [{
 			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()]
			} for movie in us_library]
# ACTION ROW
		action_library	= library.filter(genre = '2')
		action_movies 	= [{
 			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()]
			} for movie in action_library]
# COMEDY ROW
		comedy_library 	= library.filter(genre = '12')
		comedy_movies 	= [{
 			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': [service.name for service in movie.service.all()]
			} for movie in action_library]
		return JsonResponse({'theater' 	: theater_movies,
							 'watcha' 	: watcha_movies,
							 'netflix'	: netflix_movies, 
							 'kr'		: korean_movies,
							 'us'		: us_movies,
							 'action'	: action_movies,
							 'comedy'	: comedy_movies,
							}, status=200)



class RaterView(View) :
	def get(self, request) :
		library = Movies.objects.values()
		block 	= [movies for movies in library]

		return JsonResponse({'all movies': block})