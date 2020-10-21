import json
import re

from django.http import JsonResponse
from django.views import View
from user.models import User



class SignUpView(View):

    def post(self,request):
        data = json.loads(request.body)

        email_compile = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"

        try :
            if '@' not in data['email'] and '.' not in data['email'] :
                return JsonResponse({'MESSAGE' : 'EMAIL_ERROR'}, status = 400)

            elif len(data['password'] < 6 : 
                     return JsonResponse({'MESSAGE' : 'SHORT_PASSWORD'}, status = 400)

            elif Users.objects.filter(email = data['email']).exists():
                     return JsonResponse({'MESSAGE' : 'EMAIL_OVERLAP'}, status = 400)

            else :

            name = data['name']
            email = data['email']
            password = data['password']

            User.objects.create(
                name= name, 
                email= email, 
                password= password,
            )
        

