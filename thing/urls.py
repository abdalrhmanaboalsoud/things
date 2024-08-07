
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
        path('', ThingList.as_view(), name='things_list'),
        path('<int:pk>/', ThingDetail.as_view(), name='thing_detail'),
]
