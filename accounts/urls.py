from django.urls import path
from .views import login_view, register_view, logout_view, profile_view, profile_create, profile_update

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/create/', profile_create, name='profile_setup'),
    path('profile/update/', profile_update, name='profile_update'),
]