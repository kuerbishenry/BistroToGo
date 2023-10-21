from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/update/', views.profile_update, name='profile_update'),
]
