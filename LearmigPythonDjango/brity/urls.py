from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('post/<int:post_id>', views.details_post ,name='details_post'),
    path('category/<int:category_id>', views.details_category, name='details_category'),
]
