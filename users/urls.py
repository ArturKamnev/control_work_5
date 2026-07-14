from django.urls import path
from .views import RegistrationApiView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path(
        'register/',
        RegistrationApiView.as_view(),
        name='register',
    ),
    path(
        'login/',
        obtain_auth_token,
        name='login',
    ),
]