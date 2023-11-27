from django.contrib import admin
from django.urls import include, path
from learn import views as learn_views

urlpatterns = [
    path("learn/", include("learn.urls")),
    path("admin/", admin.site.urls),
    path('', learn_views.redhom, name='home'),
]