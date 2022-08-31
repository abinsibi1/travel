from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo1,name='demo'),

    # path('add/',views.addition,name='addition')
]