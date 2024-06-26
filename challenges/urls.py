from django.urls import path

from . import views

urlpatterns = [
  # path("january", views.january),
  # path("february", views.february),
  # path("march", views.march)
  
  #str and int act as path converters and order does matter here. First, it'll check for int in route and them string
  path("", views.index), # /challenges/ which is our index
  path("<int:month>", views.monthly_challenge_by_number), 
  path("<str:month>", views.monthly_challenge, name="month-challenge") #named urls
]