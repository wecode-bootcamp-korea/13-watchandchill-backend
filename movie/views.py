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
		library = Movies.objects.values()


#IN THEATERS
		theater_library 	= library.filter(in_theaters = '1')
		theater_movies  	= t_movie for t_movie in theater_library[0:20]]

#NETFLIX ROW
		netflix_library 	= library.filter(service = '1')
		netflix_movies  	= [n_movie for n_movie in netflix_library[0:20]]

#WATCHA ROW
		watcha_library  	= library.filter(service = '2')
		watcha_movies 		= [w_movie for w_movie in watcha_library[0:20]]

#US-BEST ROW
		us_library			= library.filter(country = '미국')
		us_movies 			= [us_movie for us_movie in us_library[0:20]]

#KOREA-BEST ROW
		kr_library 			= library.filter(country = '한국')
		kr_movies 			= [kr_movie for kr_movie in kr_library[0:20]]

#EXCITING ACTION ROW
		action_library		= library.filter(genre = '2')
		action_movies		= [a_movie for a_movie in action_library[0:20]]


		return JsonResponse({'netflix': netflix_movies, 'watcha': watcha_movies, 'action': action_movies, 'us': us_movies, 'kr': kr_movies}, status=200)

class RaterView(View) :
	def get(self, request) :
		library = Movies.objects.values()
		block 	= [movies for movies in library]

		return JsonResponse({'all movies': block})