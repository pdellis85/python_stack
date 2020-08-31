from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('random_word', views.root),
    path('reset', views.reset)
]
