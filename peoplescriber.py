import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE","watchapedia.settings")
django.setup()

from movie.models import *

CSV_PATH_INFO = './actornames.csv'


with open(CSV_PATH_INFO) as in_file:

	data_reader = csv.reader(in_file)


	for row in data_reader:


		if row[0]:
			name 		= row[0]
			avatar_url	= row[1]
		
			People.objects.create(
				name 		 = name, 
				avatar_url	 = avatar_url, 
			)
