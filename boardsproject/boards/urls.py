from django.contrib import admin
from django.urls import path
from boards.views import home_view,boardtopics_view,newtopic_view
urlpatterns = [
  
  path('<int:board_id>/', boardtopics_view ,name='boardtopics'), 
   path('<int:board_id>/new/', newtopic_view ,name='newtopics')
]