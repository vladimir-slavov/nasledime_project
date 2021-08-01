from django.urls import path


from nasledime_project.profiles.views import RegisterUser, LoginUser, LogoutUser

urlpatterns = (
    path('register/', RegisterUser.as_view(), name='register user'),
    path('login/', LoginUser.as_view(), name='login user'),
    path('logout/', LogoutUser.as_view(), name='logout'),
)