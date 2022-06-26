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
