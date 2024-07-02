from django.urls import path
from tasks.views import *

urlpatterns = [
    path('list', tasks, name="tasks"),
    path('<int:pk>', task, name="task"),
    path('edit/<int:pk>', task_edit, name="task_edit"),
    path('delete/<int:pk>', task_delete, name="task_delete"),
]
