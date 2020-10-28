from django.urls    import path
from .views         import MoviePageRatingView

urlpatterns = [
    path('/<int:movie_id>',MoviePageRatingView.as_view())
]
