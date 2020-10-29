from django.urls import path
from .views import SignUpView, LoginView, StatusSelectorView, CountryRankView

urlpatterns = [
    path('',SignUpView.as_view()),
    path('/login',LoginView.as_view()),
    path('/status/<int:status_id>/movie/<int:movie_id>', StatusSelectorView.as_view()),
    path('/user/preference', CountryRankView.as_view()),
    ]
