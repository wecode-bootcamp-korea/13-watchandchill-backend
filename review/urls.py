from django.urls    import path
from .views         import MovieRatingView

urlpatterns = [
    path('/<int:movie_id>',MovieRatingView.as_view())
]
