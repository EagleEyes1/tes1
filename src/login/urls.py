from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.log, name='login'),
    path('logout', views.log_out, name='logout')
]