import json
import re
import bcrypt
import jwt

from django.http import JsonResponse
from django.views import View
from user.models import User
from my_settings import SECRET_KEY,ALGORITHM


class SignUpView(View):

    def post(self,request):
        data = json.loads(request.body)

        email_test      ='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        password_test   ='^[A-Za-z0-9]{6,}$'

        try :
            if re.match(email_test, data['email']) == None :
                return JsonResponse({'MESSAGE' : 'EMAIL_ERORR'}, status = 401)

            elif re.match(password_test, data['password']) == None : 
                return JsonResponse({'MESSAGE' : 'PASSWORD_ERROR'}, status = 401)

            elif User.objects.filter(email = data['email']).exists():
                return JsonResponse({'MESSAGE' : 'EMAIL_OVERLAP'}, status = 404)

            else :
                    User.objects.create(
                        name = data['name'], 
                        email = data['email'],
                        password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode())
                    return JsonResponse({'MESSAGE' : 'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 401)


class LoginView(View):

    def post(self,request):
        data = json.loads(request.body)

        try :
            if User.objects.filter(email=data['email']).exists():
                db_email= User.objects.get(email=data['email'])
                if bcrypt.checkpw(data['password'].encode('utf-8'),db_email.password.encode('utf-8')) == True:
                    return JsonResponse({'MESSAGE' : 'SUCCESS', 'AUTHORIZATION' : jwt.encode({'id' : db_email.id}, SECRET_KEY, ALGORITHM).decode()}, status=200)
                else : 
                    return JsonResponse({'MESSAGE' : 'EMAIL_OR_PASSWORD_ERROR'}, status=400)
            else :
                return JsonResponse({'MESSAGE' : 'EMAIL_DOES_NOT_EXIST'}, status=400)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status=400)
