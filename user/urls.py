from django.urls import path
from .views import SignUpView, LoginView, StatusSelector

urlpatterns = [
    path('',SignUpView.as_view()),
    path('/login',LoginView.as_view())
    path('/info/movies/<int:movie_id>/status')
]
