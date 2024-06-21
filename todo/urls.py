from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllMonsters.as_view(), name="index"),
    path("old/", views.OldMOnsters.as_view(), name="old")
]
