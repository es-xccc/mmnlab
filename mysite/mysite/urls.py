from django.contrib import admin
from django.urls import include, path
from student import views as student_views

urlpatterns = [
    path("student/", include("student.urls")),
    path("admin/", admin.site.urls),
    path('', student_views.redhom, name='home'),
]