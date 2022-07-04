from django.urls import path
from .views import (CreateLabel,
                    LabelsListView,
                    LabelDeleteView,
                    LabelUpdateView,
                    )


urlpatterns = [
    path('create/', CreateLabel.as_view(), name='label_create'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='label_update'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='label_delete'),
    path('', LabelsListView.as_view(), name='labels_list'),
]
