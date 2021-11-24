from django.urls import path
from . import views

urlpatterns = [
    path("greet", views.greet, name = "greet"),
    path("index", views.index, name = "index.html"),
    path("enock", views.enock, name = "enock"),
    path("photos", views.photos, name = "photos"),
    # path("<str:name>",views.all_greet, name="greet.html"),


  
]