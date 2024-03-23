# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('add_numbers/', views.add_numbers_view, name='add_numbers'),
    # path('task_result/', views.task_results_view, name='add_numbers'),
    # path('update-schedule/', views.update_schedule, name='update_schedule'),
    # path('', views.index, name='index'),
    path("schedule/", views.schedule_task, name="schedule")
]
