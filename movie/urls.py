from django.urls import path
from movie.views import ListView, PageView

urlpatterns = [
	path('/list', ListView.as_view()),
	path('/<int:movie_id>', PageView.as_view()),
]