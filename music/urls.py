from django.urls import path

from . import views as v

urlpatterns = [
    path('create', v.MusicByValueCreateAPIView.as_view()),
    path('all', v.MusicByValueListAPIView.as_view()),
    path('<int:pk>', v.MusicByValueDetailAPIView.as_view()),

    path('get', v.RecommendationBySongAPIView.as_view())
]
