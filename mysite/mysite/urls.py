from django.contrib import admin
from django.urls import include, path
from polls import views as polls_views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('', polls_views.login_view, name='home'),
    path('login_success/', polls_views.login_success, name='login_success'),
]