from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scholarship/<int:id>/detail', views.scholarship, name='view_scholarship'),
]
