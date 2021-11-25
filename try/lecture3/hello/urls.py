from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>", views.index, name = "index"),

    path("<str:name>", views.greet, name = "greet",),
    path("enock", views.enock, name = "enock"),
    path("photos", views.photos, name = "photos"),
    # path("<str:name>",views.all_greet, name="greet.html"),


  
]