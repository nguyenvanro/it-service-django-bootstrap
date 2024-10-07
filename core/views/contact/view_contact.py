
from django.shortcuts import render
from django.views import View


class ContactView(View):
    def get(self,request):

        context = {

        }
        return render(request, 'contact/contact.html', context)
    def post(self, request):
        pass