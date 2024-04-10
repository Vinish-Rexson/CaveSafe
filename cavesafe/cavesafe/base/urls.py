from django.urls import path
from base import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('login',views.login,name="login"),
    path('index',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('kgf',views.kgf,name="kgf"),
    path('form',views.form,name="form"),
    path('bugs',views.bugs,name="bugs"),
    path('geo',views.geo,name="geo"),
    path('emerg',views.emerg,name="emerg"),
    path('chat',views.chat,name="chat"),
    path('profile',views.profile,name="profile"),
]