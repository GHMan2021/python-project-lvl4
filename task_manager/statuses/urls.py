from django.urls import path
from .views import *


urlpatterns = [
    path('create/', CreateStatus.as_view(), name='status_create'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('', StatusesListView.as_view(), name='statuses_list'),
]