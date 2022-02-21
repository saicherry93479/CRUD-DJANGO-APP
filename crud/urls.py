from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path("completed/<int:pk>",views.completed,name="completed"),
    path("deleted/<int:pk>",views.deleted,name="deleted"),
    path("completeUndo/<int:pk>",views.completeUndo,name="completeUndo"),
    path("deleteUndo/<int:pk>",views.deleteUndo,name="deleteUndo"),
]
