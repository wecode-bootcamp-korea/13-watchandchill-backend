from django.urls import path
from movie.views import ListView, PageView

urlpatterns = [
	path('/list', ListView.as_view()),
	path('/page', PageView.as_view()),
]