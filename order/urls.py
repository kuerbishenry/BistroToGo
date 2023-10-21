from django.conf.urls.static import static
from django.conf import settings 
from django.contrib.auth import views as auth_views

from django.urls import include, path

#from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import LoginView
from . import views

app_name = "order"

urlpatterns = [
    path('', views.index, name='order'),  
]