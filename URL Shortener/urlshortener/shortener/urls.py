from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create),
    path('s/<str:short_url>', views.redirect),
]