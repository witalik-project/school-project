from django.urls import path
from . import views

app_name = "points"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("school/class/create", views.CreateClass.as_view(), name="class_create"),
    path("school/class/edit/<int:pk>", views.EditClass.as_view(), name="class_edit"),
    path("school/class/delete/<int:pk>", views.DeleteClass.as_view(), name="class_delete"),
    path("school/points/log/create", views.create_points_log, name="points_log_create"),
    path("school/points/add/log/create/<int:pk>", views.add_points_log, name="points_add_log_create"),
    path("school/points/subtract/log/create/<int:pk>", views.subtract_points_log, name="points_substract_log_create"),
    path("school/points/log/history", views.LogsList.as_view(), name="points_logs_history"),
    path("school/points/log/delete", views.delete_logs, name="points_log_delete"),
    path("school/scoreboard/", views.Scoreboard.as_view(), name="scoreboard"),
]
