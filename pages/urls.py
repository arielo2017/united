from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name= 'about'),
    path('admin/', admin.site.urls),
    path('users/', views.usersList.as_view()),
    path('matches/', views.matchMakingList.as_view())

]