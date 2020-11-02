from django.urls import path
from .views import SignUpView, LoginView, StatusSelectorView, PreferenceView, ProfileView


urlpatterns = [
    path('',SignUpView.as_view()),
    path('/login',LoginView.as_view()),

    path('/status/<int:status_id>/movie/<int:movie_id>', StatusSelectorView.as_view()),
    path('/preference', PreferenceView.as_view()),
    path('/profile',ProfileView.as_view())
    ]
