from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about_us, name='about_us'),
     
     path('blog/', views.blog, name="blog_page"),
     path('blog/<int:blog_id>/', views.blog, name="blog_page"),
    
     path('team/', views.team_page, name='team'),

     path('practice-area/<slug:slug>/', views.practice_area_detail, name='practice_area_detail'),
     path('careers/', views.careers, name='careers'),
]