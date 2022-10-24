from django.urls import path
from . import views

urlpatterns = [
   path("", views.index),
   path("school/class/edit/<int:pk>", views.EditClass.as_view()),
   path("school/class/delete/<int:pk>", views.DeleteClass.as_view()),
   path("school/points/add/log/create/<int:pk>", views.add_points_log),
   path("school/points/subtract/log/create/<int:pk>", views.subtract_points_log),
   path("school/scoreboard", views.Scoreboard.as_view()),
   path("login", views.login_request, name="login"),
   path("logout", views.logout_request, name="logout"),
   path("school/points/log/history", views.LogsList.as_view()),
]
