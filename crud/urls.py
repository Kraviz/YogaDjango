from django.urls import path
from . import views

urlpatterns = [
    path('addprod', views.create_view),
]