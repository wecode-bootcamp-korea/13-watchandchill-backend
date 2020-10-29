from django.urls    import path
from .views         import (
    ReviewView,
    StarRatingView,
    MovieRatingView
    )


urlpatterns = [
    path('/<int:movie_id>',MovieRatingView.as_view()),
    path('/rating', StarRatingView.as_view()),
    path('/get', ReviewView.as_view())
]
