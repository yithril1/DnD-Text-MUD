# pages/urls.py
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    url(r'^get_max_chars$', views.get_max_chars),
    path('profile/<int:pk>', views.CharacterDetailView.as_view(), name="character-detail")
]