from django.contrib import admin
from django.urls import path, include

from task_manager import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='/'),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('users/', include('task_manager.users.urls')),
]

urlpatterns += [
    path('statuses/', include('task_manager.statuses.urls')),
]

urlpatterns += [
    path('tasks/', include('task_manager.tasks.urls')),
]

urlpatterns += [
    path('labels/', include('task_manager.labels.urls')),
]
