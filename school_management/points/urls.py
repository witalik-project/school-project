from django.urls import path
from . import views

urlpatterns = [
   path('', views.Index.as_view()),
   path('school/class/create', views.CreateClass.as_view()),
   path('school/class/edit/<int:pk>', views.EditClass.as_view()),
   path('school/class/delete/<int:pk>', views.DeleteClass.as_view()),
   path('school/points/log/create', views.create_points_log),
]
