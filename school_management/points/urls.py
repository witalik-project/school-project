from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("school/class/create", views.CreateClass.as_view()),
    path("school/class/edit/<int:pk>", views.EditClass.as_view()),
    path("school/points/log/create", views.create_points_log),
    path("school/class/delete/<int:pk>", views.DeleteClass.as_view()),
    path("school/points/add/log/create/<int:pk>", views.add_points_log),
    path("school/points/subtract/log/create/<int:pk>", views.subtract_points_log),
    path("school/scoreboard", views.Scoreboard.as_view(), name="scoreboard"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("school/points/log/history", views.LogsList.as_view(), name="logs_history"),
    path("school/points/log/delete", views.delete_logs, name="delete_logs"),
]
