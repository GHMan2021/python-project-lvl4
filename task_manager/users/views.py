from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
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


class RegisterUser(CreateView):
    form_class = CustomUserForm
    template_name = 'users/user_add.html'
    success_url = reverse_lazy('/')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('/')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('/')


class UserloginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_message = 'Вы залогинены!'


class UserLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'Вы разлогинены!')
        return super().dispatch(request, *args, **kwargs)
