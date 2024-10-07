
from django.urls import path
from core.views.home import view_home
from core.views.blog import view_blog
from core.views.contact import view_contact
from core.views import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', view_home.Home.as_view(), name='home'),

    path('contact',view_contact.ContactView.as_view(), name='contact'),

    path('blog', view_blog.BlogView.as_view(), name='blog'),

    path('blog-detail', view_blog.BlogDetailView.as_view(), name='blog-detail'),

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
