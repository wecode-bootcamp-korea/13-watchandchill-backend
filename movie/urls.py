from django.urls import path
from movie.views import ListView, RaterView

urlpatterns = [
	path('/list', ListView.as_view()),
	path('/rater', RaterView.as_view()),
]