from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserForm
from .models import CustomUser


class UsersListView(ListView):
    model = CustomUser
    template_name = 'users/users_list.html'
    context_object_name = 'users_list'


class RegisterUser(SuccessMessageMixin, CreateView):
    form_class = CustomUserForm
    template_name = 'users/user_add.html'
    success_url = reverse_lazy('login')
    success_message = "Пользователь успешно зарегистрирован"


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users_list')
    success_message = "Пользователь успешно изменён"


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CustomUser
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users_list')
    success_message = "Пользователь успешно удалён"
