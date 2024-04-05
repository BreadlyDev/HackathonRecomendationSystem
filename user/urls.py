from django.urls import path
from . import views as v

urlpatterns = [
    path('register', v.RegisterAPIView.as_view()),
    path('login', v.LoginAPIView.as_view()),
    path('logout', v.LogoutAPIView.as_view()),

    path('profile/all', v.ProfileListAPIView.as_view()),
    path('profile/me', v.ProfileDetailAPIView.as_view()),
]
