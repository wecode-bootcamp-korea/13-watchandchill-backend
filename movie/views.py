#Python
import json
#Django
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
#Custom
from movie.models import Movies, MoviePhotos, MovieVideos, Cast, People, Genres, MovieGenres, Tags, MovieTags, Services, MovieServices


class FrontView(View):
	def get(self, request) :
		def info_lister(filtered_list):
			info = [{
			'id' 	 : movie.id,
			'title'  : movie.title,
			'date'	 : movie.premier_date,
			'country': movie.country,
			'poster' : movie.poster_url,
			'runtime': movie.run_time,
			'service': list(movie.service.values_list('name',flat= True)),
			'genre'	 : list(movie.genre.values_list('name', flat= True))
			} for movie in filtered_list[:20]]
			return info
		library = Movies.objects.all()
#IN THEATERS
		library_listed 		= [titles for titles in library]
		theater_filtered 	= [title for title in library if title.in_theaters== 1]
#WATCHA ROW
		watcha_filtered 	= library.filter(service = '2')
#NETFLIX ROW
		netflix_filtered	= library.filter(service = '1')
#KOREA-BEST ROW
		library_listed 		= [titles for titles in library]
		korea_filtered 		= [title for title in library if title.country == '한국']
#US-BEST ROW
		library_listed 		= [titles for titles in library]
		us_filtered 	   	= [title for title in library if title.country == '미국']
#ACTION ROW
		action_filtered	= library.filter(genre = '2')
#COMEDY ROW
		comedy_filtered 	= library.filter(genre = '12')

		return JsonResponse ({
							'theater'	: info_lister(theater_filtered),
							'watcha' 	: info_lister(watcha_filtered),
							'netflix'	: info_lister(netflix_filtered), 
							'kr'		: info_lister(korea_filtered),
							'us'		: info_lister(us_filtered),
							'action'	: info_lister(action_filtered),
							'comedy'	: info_lister(comedy_filtered),
							}, status=200)

# class MoviesView(View):
# 	def get(self, request) :
# 		def info_lister(filtered_list):
# 			info = [{
# 			'id' 	 : movie.id,
# 			'title'  : movie.title,
# 			'date'	 : movie.premier_date,
# 			'country': movie.country,
# 			'poster' : movie.poster_url,
# 			'runtime': movie.run_time,
# 			'service': list(movie.service.values_list('name',flat= True)),
# 			'genre'	 : list(movie.genre.values_list('name', flat= True))
# 			} for movie in filtered_list[:20]]


class MovieView(View) :
	def get(self, request, movie_id) :
		try:
			data 	 	= json.loads(request.body)
			movie 	 	= Movies.objects.get(id = movie_id)
			all_info 	={
				'id'			: movie.id,
				'title'			: movie.title,
				'date'			: movie.premier_date,
				'poster_url'	: movie.poster_url,
				'country'		: movie.country,
				'service'		: list(movie.service.values()),
				'genre'			: list(movie.genre.values_list('name', flat=True)),
				'photos'		: [photos.photo_url for photos in movie.moviephotos_set.all()],
				'videos'		: [videos.video_url for videos in movie.movievideos_set.all()],
				'tag'			: list(movie.genre.values_list('name', flat=True)),
				'runtime'		: movie.run_time,
				'coverpic_url'	: movie.coverpic_url,
				'description'	: movie.description,
				'cast'			: [{
									'name': person.name, 
									'role': Cast.objects.filter(movie = movie , name = person)[0].role, 
									'cast_as': Cast.objects.filter(movie = movie , name = person)[0].cast_as, 
									'photo': person.avatar_url
									} 
				for person in movie.casting.all()]
		
			}
			return JsonResponse ({'movie_information': all_info}, status=200)
		except Movies.DoesNotExist:
			return JsonResponse ({'KeyError': 'Non-existant movie id'}, status = 404)

class ActorView(View) :
	def get(self, request, person_id) :
		try:
			person 		= People.objects.get(id = person_id)
			movie_list 	= [{
				'movie_id'	: cast.movie.id,
				'title'		: cast.movie.title,
				'poster_url': cast.movie.poster_url,
				'services'	: [{'name': info.name, 'logo': info.icon_url} for info in cast.movie.service.all()]
				} for cast in Cast.objects.filter(name = person)
			]
			person_info = {
				'id'		: person.id,
				'name'		: person.name,
				'pic_url' 	: person.avatar_url,
				'movie_list': list(movie_list)
			}
			return JsonResponse({'filmography': person_info}, status=200)
		except People.DoesNotExist:
			return JsonResponse ({'KeyError': 'Non-existant person'}, status=404)