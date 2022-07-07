from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'task_manager/index.html'


class UserloginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_message = 'Вы залогинены!'


class UserLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'Вы разлогинены!')
        return super().dispatch(request, *args, **kwargs)
