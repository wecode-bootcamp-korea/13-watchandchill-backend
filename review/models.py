from django.db import models
from user.models import User
from movie.models import Movies


class StarRating(models.Model):
    user = models.ForeignKey('user.User', on_delete = models.CASCADE)
    movie = models.ForeignKey('movie.Movies', on_delete = models.CASCADE)
    star_rating = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta :
        db_table = 'star_ratings'


class Comment(models.Model):
    user = models.ForeignKey('user.User', on_delete = models.CASCADE)
    movie = models.ForeignKey('movie.Movies', on_delete = models.CASCADE)
    content = models.CharField(max_length = 500)

    class Meta :
        db_table = 'comments'

class CommentLike(models.Model):
    user = models.ForeignKey('user.User', on_delete = models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete = models.CASCADE)

    class Meta :
        db_table = 'comments_likes'

