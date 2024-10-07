
from django.shortcuts import render
from django.views import View


class BlogView(View):
    def get(self,request):

        context = {

        }
        return render(request, 'blog/blog.html', context)
    def post(self, request):
        pass

class BlogDetailView(View):
    def get(self,request):

        context = {

        }
        return render(request, 'blog/blog-details.html', context)
    def post(self, request):
        pass