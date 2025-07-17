from django.contrib import admin
from django.urls import path
from . import views

#NOTE: where to setup the paths to call from react to get a request
# adding to the url patterns
# 1st: is the domain/(goes here) , 2nd: the correct views file, 3rd:
urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('logout/', views.logout_user, name='logout_user'), 
    path('water-bodies/', views.water_bodies, name="water_bodies"), #BOW info
    path('fish-types/', views.fish_types, name="fish_types"), # for fish info
    path('bait-types/', views.bait_types, name="bait_types"), # for bait info
    path('submit-fish/', views.submit_fish, name="submit_fish"),
    path('submit-bait/', views.submit_bait, name="submit_bait"), 
    path('submit-catch/', views.submit_catch , name='submit_catch'),
    path('get-fishing-logs/', views.get_fishing_logs, name="get_fishing_logs")
]
