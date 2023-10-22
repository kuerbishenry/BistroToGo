from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('update-profile/', views.profile_update, name='profile_update'),
    path('order/', views.select_option_view, name='order'),
    path('pickfood/',views.order, name='pickfood' )
]
