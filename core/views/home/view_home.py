from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views import View

from core.models import Contact
from django.core.exceptions import ValidationError

class Home(View):
    def get(self,request):

        context = {

        }
        return render(request, 'home/index.html', context)
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        country = request.POST['country']
        numberphone = request.POST['numberphone']
        description = request.POST['description']
        data = Contact(name=name, email=email, country=country, numberphone=numberphone, description=description)
        try:
            data.full_clean()
            data.save()
            context = {
                'message':  name,
                'result':'success',
            }
            return JsonResponse(context, status=200 )

        except ValidationError as e:

            context = {
                'message': e,
                'result':'error',
            }
        return JsonResponse(context, status=200)