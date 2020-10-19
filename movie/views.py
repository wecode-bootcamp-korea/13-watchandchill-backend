#Python
import json
#Django
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
#Custom
from movie.models import *


class MoviesView(View):
	def post(self, request):