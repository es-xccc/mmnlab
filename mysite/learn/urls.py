from django.urls import path
from . import views

urlpatterns = [
    path('st_register/', views.st_register, name='st_register'),
    path('st_login/', views.st_login, name='st_login'),
    path('home/', views.home, name='home'),
    path('ib_learning/', views.ib_learning, name='ib_learning'),
    path('monitor/', views.monitor, name='monitor'),
    path('logout/', views.logout_view, name='logout_view'),
    path('get_last_line/', views.get_last_line, name='get_last_line'),
]