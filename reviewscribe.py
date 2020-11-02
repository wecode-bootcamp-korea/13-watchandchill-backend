import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE","watchapedia.settings")
django.setup()

from movie.models import *
from review.models import *

CSV_PATH_INFO = './reviews.csv'


with open(CSV_PATH_INFO) as in_file:

	data_reader = csv.reader(in_file)
	next(data_reader,'\ufeff')


	for row in data_reader:


		if row[0]:
			user_id 		= row[0]
			movie_id 		= row[1]
			star_rating	 	= row[2]
		
			StarRating.objects.create(
				user_id 	 = user_id, 
				movie_id 	 = movie_id,
				star_rating  = star_rating 
			)
