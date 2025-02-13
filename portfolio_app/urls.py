from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blog/', views.blog_post, name='blog_post'),
]
