from django.urls import path
from . import views
# URLConf or URL Configuration
urlpatterns = [
    path('hello/', views.say_hello),
    path('intro/', views.introduction),
    path('draughts/', views.play_draughts)
]
