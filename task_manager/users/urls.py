from django.urls import path
from .views import (RegisterUser,
                    UsersListView,
                    UserDeleteView,
                    UserUpdateView,
                    )


urlpatterns = [
    path('create/', RegisterUser.as_view(), name='user_add'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('', UsersListView.as_view(), name='users_list'),
]
