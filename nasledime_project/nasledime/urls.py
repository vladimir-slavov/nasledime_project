from django.urls import path

from nasledime_project.nasledime import views

urlpatterns = (
    path('', views.IndexView.as_view(), name='index'),
)