import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE","watchapedia.settings")
django.setup()

from movie.models import *

CSV_PATH_INFO = './movieinfo.csv'


with open(CSV_PATH_INFO) as in_file:

	data_reader = csv.reader(in_file)


	for row in data_reader:


		if row[0]:
			titles 		= row[0]
			premiers	= row[1]
			countrys 	= row[2]
			run_times	= row[3]
			poster_urls	= row[4]
			services 	= row[5].split('+')
			genres 		= row[6].split('+')
			tags 		= row[7].split('+')
			in_theaters = row[8]

		
			movie, created = Movies.objects.get_or_create(
				title 		 = titles, 
				premier_date = premiers, 
				country 	 = countrys, 
				run_time 	 = run_times, 
				poster_url 	 = poster_urls, 
				in_theaters  = in_theaters
			)

			for genre in genres:
				genre1 ,created = Genres.objects.get_or_create(name = genre)
				MovieGenres.objects.get_or_create(movie = movie, genres = genre1)


			for service in services:
				serve1 ,created = Services.objects.get_or_create(name = service)
				MovieServices.objects.get_or_create(movie = movie, service = serve1)

			for tag in tags:
				tag1 ,created = Tags.objects.get_or_create(name = tag)
				MovieTags.objects.get_or_create(movie = movie, tag = tag1)