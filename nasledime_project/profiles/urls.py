from django.urls import path

from nasledime_project.profiles.views import RegisterUser

urlpatterns = (
    path('register/', RegisterUser.as_view(), name='register user'),
)