from django.conf.urls import url
from django.contrib import admin

from .views import CreatePlaceAPIView,ViewPlaceAPI,UniquePlaceAPI

urlpatterns = [
    url(r'CreatePlace/', CreatePlaceAPIView.as_view(), name='create'), 
    url(r'ViewPlace/', ViewPlaceAPI.as_view(), name='View'), 
    url(r'UniquePlace/',UniquePlaceAPI.as_view(),name='unique')  
]