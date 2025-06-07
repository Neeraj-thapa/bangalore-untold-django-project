from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    


    path('home/', views.home, name='home'),
    path('user_submissions/', views.user_submissions, name='user_submissions'),
    path('events/', views.event_list, name='events'),
    path('blogs/', views.blog_list, name='blog'),
    

    path('explore/', views.explore, name='explore'),
    path('map/', views.map_view, name='map'),
    path('faq/', views.faq, name='faq'),
    path('explore/nature/', views.nature, name='nature'),
    path('explore/markets/', views.markets, name='markets'),
    path('explore/historic/', views.historic, name='historic'),
    path('explore/cafes/', views.cafes, name='cafes'),
]
