from django.urls import path

from nasledime_project.nasledime import views
from nasledime_project.nasledime.views import IndexView, CreateWill, \
    HowWillsWorkView, ListAllWillsView, WillDetailView, EditWillView, DeleteWillView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('how-wills-work/', HowWillsWorkView.as_view(), name='how wills work'),
    path('create-will/', CreateWill.as_view(), name='create will'),
    path('update-will/<int:pk>/', EditWillView.as_view(), name='edit will'),
    path('delete-will/<int:pk>/', DeleteWillView.as_view(), name='delete will'),
    path('all-wills/', ListAllWillsView.as_view(), name='wills list'),
    path('will-details/<int:pk>/', WillDetailView.as_view(), name='will details'),
)