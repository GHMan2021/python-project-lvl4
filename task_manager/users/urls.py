from django.urls import path
from .views import *

urlpatterns = [
    # path('', UsersListView.as_view(), name='users_list'),
    path('create/', RegisterUser.as_view(), name='user_add'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('login/', UserloginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('', UsersListView.as_view(), name='users_list'),
]
