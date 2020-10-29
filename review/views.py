import json
import random

from django.http        import JsonResponse
from django.views       import View
from django.db.models   import Count

from review.models      import StarRating
from user.models        import User
from movie.models       import *
from my_settings        import SECRET_KEY,ALGORITHM
from user.utils         import login_decorator



class ReviewView(View):
    @login_decorator
    def get(self, request) :
        #data        = json.loads(request.body)
        user_id     = request.user.id
        genre       = request.GET.get("genre", None)
        offset      = int(request.GET.get("offset", "0"))
        limit       = int(request.GET.get("limit", "20"))

        if not MovieGenres.objects.filter(genres_id = genre).exists() :
            user_rating     = StarRating.objects.filter(user = user_id)
            rating_movies   = [movie.movie.id for movie in user_rating]
            movie_list      = Movies.objects.all().exclude(id__in = rating_movies)


            movies = [{ 'id'        : movie.id,
                       'title'      : movie.title,
                       'poster'     : movie.poster_url,
                       'date'       : movie.premier_date,
                       'country'    : movie.country} for movie in movie_list][offset:offset+limit]
            random.shuffle(movies)

            count = StarRating.objects.filter(user=user_id).count()

            return JsonResponse({"MOVIES_RANDOM" : movies,"COUNT" : count},status = 200) 

        else :
            category = MovieGenres.objects.filter(genres_id = genre)
            category_movies = [movie.movie.id for movie in category]
            star_movie = StarRating.objects.filter(user = user_id, movie__in = category_movies)
            s_movie_list = [movie.movie.id for movie in star_movie]
            real_movies = Movies.objects.all().exclude(id__in = s_movie_list)
            movies = [{ 'id' : movie.id,
                       'title' : movie.title,
                       'poster' : movie.poster_url,
                       'date' : movie.premier_date,
                       'country' : movie.country} for movie in real_movies][offset:offset+limit]

            return JsonResponse({"MOVIES" : movies}, status = 200)


            """
            genre = {'0' : 랜덤영화'
            '1' : '느와르',
                 '2' : '액션',
                 '3' : '판타지',
                 '4' : 'SF',
                 '5' : '가족',
                 '6' : '드라마',
                 '7' : '슈퍼히어로',
                 '8' : '애니메이션',
                 '9' : '범죄',
                 '10' : '공포',
                 '11' : '로맨틱코미디',
                 '12' : '코미디',
                 '13' : '로맨스',
                 '14' : '다큐멘터리',
                 '15' : '클래식',
                 '16' : '스릴러',
                 '17' : '전쟁'}
            """


class StarRatingView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user_id = request.user.id
            movie_id = data["movie_id"]
            star_rating   = data["star_rating"]

            if not StarRating.objects.filter(user_id=user_id, movie_id=movie_id).exists():
                StarRating.objects.create(
                    user_id  = user_id,
                    movie_id = movie_id,
                    star_rating = star_rating
                    )
                count = StarRating.objects.filter(user=user_id).count()
                return JsonResponse({'MESSAGE':'POST_SUCCESS','COUNT' : count}, status=201)
            return JsonResponse({'MESSAGE':'star rating is exists'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=404)

    @login_decorator
    def patch(self, request):
        try:
            data = json.loads(request.body)
            user_id = request.user.id
            movie_id = data["movie_id"]
            star_rating = data["star_rating"]

            if StarRating.objects.filter(user_id = user_id, movie_id = movie_id).exists():
                StarRating.objects.filter(
                    user_id  = user_id,
                    movie_id = movie_id
                ).update(star_rating=star_rating)
                return JsonResponse({'MESSAGE':'PATCH_SUCCESS'}, status=200)
            return JsonResponse({'MESSAGE':'star rating is exists'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=404)

    @login_decorator
    def delete(self, request): 
        try:
            data = json.loads(request.body)
            user_id = request.user.id
            movie_id = data["movie_id"]
            star_rating = data["star_rating"]
 
            rating = StarRating.objects.filter(user_id  = user_id, movie_id = movie_id)

            if rating.exists() and rating.get().star_rating == star_rating :
                rating.delete()
                count = StarRating.objects.filter(user=user_id).count()
                return JsonResponse({'MESSAGE':'DELETE_SUCCESS','COUNT' : count}, status=200)
            return JsonResponse({'MESSAGE':'star rating is not exists'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=404)
        


# 데코레이터 확인 완료 (무비 상세페이지)
class MovieRatingView(View):
    @login_decorator
    def post(self, request, movie_id):
        data = json.loads(request.body)
        user_id = request.user.id
        if StarRating.objects.filter(user = user_id, movie = movie_id).exists() :
           target_movie = StarRating.objects.get(user = user_id, movie = movie_id)
           #target_movie.star_ratings

           if StarRating.objects.get(user = user_id, movie = movie_id).star_rating == data['star_rating'] :
               StarRating.objects.filter(user = user_id, movie = movie_id).delete()
               return JsonResponse({'MESSAGE' : 'DATA_DELETE'})

           else:
               star_review = StarRating.objects.get(user = user_id, movie = movie_id)
               star_review.star_rating = data['star_rating']
               star_review.save()
               return JsonResponse({'MESSAGE' : 'STAR_RATING_UPDATE'})

        else :
            user_name = User.objects.get(id = user_id)
            movie_rating_id = Movies.objects.get(id = movie_id) 
            StarRating.objects.create(user = user_name,
                                      movie = movie_rating_id,
                                      star_rating = data['star_rating']) 
            return JsonResponse({'MESSAGE' : 'STAR_RATING_ADD'}, status = 201)




