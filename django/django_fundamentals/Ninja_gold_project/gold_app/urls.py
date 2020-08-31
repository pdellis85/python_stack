from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('reset', views.reset),
    path('gold', views.process_gold)
]
