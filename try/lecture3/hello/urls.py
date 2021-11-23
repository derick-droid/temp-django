from django.urls import path
from . import views

urlpatterns = [
    # path("",views.all_greet, name="all_greet"),
    # path("greet", views.greet, name = "greet.html"),
    path("", views.index, name = "index"),
    # path("enock", views.enock, name = "enock"),
    # path("photos", views.photos, name = "photos"),
  
]