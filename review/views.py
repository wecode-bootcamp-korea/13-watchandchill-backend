import json
import random

from django.http        import JsonResponse
from django.views       import View

from review.models      import StarRating
from user.models        import User
from movie.models       import Movies
from my_settings        import SECRET_KEY,ALGORITHM
from user.utils         import login_decorator



class ReviewView(View):
    @login_decorator
    def get(self, request) :
        data = json.loads(request.body)
        user_id = request.user.id
        #리뷰페이지에서는 movie_id를 url로 받아올 수 없음 movie_id = request.GET.get("movie_id", None)
        genre  = request.GET.get("genre", None)
        offset = int(request.GET.get("offset", "0"))
        limit = int(request.GET.get("limit", "20"))

        user_rating = StarRating.objects.filter(user = 1)
        rating_movies = [movie.movie.id for movie in user_rating]
        movie_list = Movies.objects.all().exclude(id__in = rating_movies)
        movies = [{ 'id' : movie.id,
                   'title' : movie.title,
                   'poster' : movie.poster_url,
                   'date' : movie.premier_date,
                   'country' : movie.country} for movie in movie_list]
        random.shuffle(movies)

        category = {'1' : '느와르',
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
                    '17' : '전쟁',
                    '18' : '랜덤영화'}

        if genres == 18 :
            random.choice(tuple(moives.item()))

        category = MovieGenres.objects.filter(genres_id=gener)
        category_movies = [movie.






        movies = [movie for movie in movie_exist]

        if not StarRating.objects.filter(user = 1).movie.exists():


        data_movie = Movies.objects.exclude(movie = movie_exist)
        data = Movie.objects.get(movie = movie_id)
        star_rating = StarRating.objects.get(user = user_id, movie = movie_id)

        if star_rating :
            star_rating.star_rating

        elif category :
            category = Movie.objects.get(뭘로 영화 장르를 가져와야하는지 모르겠다)

class StarRatingView(View):
    @login_decorator
    def post(self, request, movie_id, star_rating):
        data = json.loads(request.body)
        user_id = request.user.id
        movie_id = request.POST.get("movie_id", None)
        star_data = request.POST.get("star_rating", None) 별점이 url로 들어오고..json data랑 헷갈린다.

        star_review = StarRating.objects.get(user = user_id, movie = movie_id)
        star_review.star_rating = data['star_rating']
        star_review.save()
        return JsonResponse({'MESSAGE' : 'STAR_RATING_UPDATE'})

    def patch(self, request, movie_id, star_rating):


    def delete(self, request, movie_id, star_rating): 


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



"""
# 영화 상세 페이지 별점 - 데코레이터 확인 필요
class MoviePageRatingView(View):
   # @login_decorator

    def post(self, request, movie_id):
        data = json.loads(request.body)

        #user_id = request.user

        if StarRating.objects.filter(user = data['user_id'], movie = movie_id).exists() :
           target_movie = StarRating.objects.get(user = data['user_id'], movie = movie_id)
           #target_movie.star_ratings

           if StarRating.objects.get(user = data['user_id'], movie = movie_id).star_rating == data['star_rating'] :
               StarRating.objects.filter(user = data['user_id'],movie = movie_id).delete()
               return JsonResponse({'MESSAGE' : 'DATA_DELETE'})

           else:
               star_review = StarRating.objects.get(user = data['user_id'], movie = movie_id)
               star_review.star_rating = data['star_rating']
               star_review.save()
               return JsonResponse({'MESSAGE' : 'STAR_RATING_UPDATE'})

        else :
            user_name = User.objects.get(id = data['user_id'])
            movie_rating_id = Movies.objects.get(id = movie_id) 
            StarRating.objects.create(user = user_name,
                                      movie = movie_rating_id,
                                      star_rating = data['star_rating']) 
            return JsonResponse({'MESSAGE' : 'STAR_RATING_ADD'}, status = 201)

"""




"""
class EvaluteView(View):
   # @login_decorator

    def post(self, request, movie_id):
        data = json.loads(request.body)

        if StarRating.objects.filter(Q(user = data['user']) & Q(movie = data['movie'])).exists() :
            if data['star_rating'] ==  StarRating.objects.fitler(star_rating = data['star_rating']) :
                StarRating.objects.filter(Q(user = data['user']) & Q(movie = data['movie'])).star_rating.delete()
                return JsonResponse({'MESSAGE' : 'STAR_RATING_DELETE'})
            else:
                star_review = StarRating.objects.filter(Q(user = data['user']) & Q(movie = data['movie'])).id
                star_review.star_rating = data['star_rating']
                star_review.save()
            return JsonResponse({'MESSAGE' : 'STAR_RATING_UPDATE'})

        else :
            StarRating.objects.create(user = data['user'],
                                      movie = data['movie'],
                                      star_rating = float(data['star_rating'])) 
            return JsonResponse({'MESSAGE' : 'STAR_RATING_ADD'}, status = 201)
