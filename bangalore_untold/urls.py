from django.contrib import admin
from django.urls import path
from django.urls import path, include
from submissions.views import home, landing,blog, add_blog, user_submissions, faq, submit_feedback,explore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('submissions.urls')), 
   
    path('', landing, name='landing'),

    path('home/', home, name='home'),
    path('blog/', blog, name='blog'),
    path('add-blog/', add_blog, name='add_blog'),
    path('submit/', user_submissions, name='user_submissions'),
    path('faq/', faq, name='faq'),
    path('submit-feedback/', submit_feedback, name='submit_feedback'),
]
