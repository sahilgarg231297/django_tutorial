from django.conf.urls import url
from first_app import views
from django.urls import path

urlpatterns = [
    path("index/", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
]

