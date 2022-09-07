from django.urls import path
from . import  views
urlpatterns = [
    path('', views.index_get,name='index'),
    path('predict/', views.predict,name='predict'),


]