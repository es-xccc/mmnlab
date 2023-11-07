from django.contrib import admin
from django.urls import include, path
from polls import views as polls_views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('', polls_views.redhom, name='home'),
]