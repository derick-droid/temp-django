from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>",views.all_greet, name="all_greet"),
    path("greet", views.greet, name = "greet"),
    path("index", views.index, name = "index"),
    path("enock", views.enock, name = "enock"),
    path("photos", views.photos, name = "photos"),
  
]