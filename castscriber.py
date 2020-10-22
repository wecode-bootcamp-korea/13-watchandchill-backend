import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE","watchapedia.settings")
django.setup()

from movie.models import *

CSV_PATH_INFO = './cast.csv'


with open(CSV_PATH_INFO) as in_file:

	data_reader = csv.reader(in_file)
	next(data_reader,'\ufeff1')

	for row in data_reader:


		if row[0]:
			name 	= row[0]
			role	= row[1]
			cast_as	= row[2]
			movie 	= row[3]

			name1	= People.objects.get(id = name)
			movie1 	= Movies.objects.get(id= movie)
		
			Cast.objects.create(
				name 	 = name1, 
				role	 = role,
				cast_as  = cast_as,
				movie    = movie1,
			)
