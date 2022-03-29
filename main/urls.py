from django.urls import path
from main import views

urlpatterns = [
    path('image/upload/', views.ImageUpload.as_view()),
    path("note/", views.Notes.as_view()),
    path("login/", views.Login.as_view()),
]
