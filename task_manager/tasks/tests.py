from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Task
from task_manager.statuses.models import Status


class TaskTestCase(TestCase):

    fixtures = ['user.json', 'status.json', 'task.json']

    def setUp(self):
        user_logged = get_user_model().objects.first()
        self.client.force_login(user_logged)

    def test_tasks_list(self):
        response = self.client.get(reverse('tasks_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/tasks_list.html')

    def test_tasks_detail(self):
        task = Task.objects.first()
        response = self.client.get(reverse('task_detail', args=[task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/task_detail.html')

    def test_task_create(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/task_create.html')

        status = Status.objects.first()
        user = get_user_model().objects.first()
        task_data_test = {
            'name': 'name_test2',
            'description': 'describe for task_test2',
            'status': status.pk,
            'executor': user.pk,
            }
        response = self.client.post(reverse('task_create'), data=task_data_test)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks_list'))
        self.assertEqual(Task.objects.count(), 2)

        task = Task.objects.last()
        self.assertEqual(task.name, 'name_test2')
        self.assertEqual(task.description, 'describe for task_test2')
        self.assertEqual(task.status.name, 'status_test')
        self.assertEqual(task.executor.username, 'username_test')
        self.assertEqual(task.author.username, 'username_test')

    def test_task_update_author(self):
        task = Task.objects.first()
        response = self.client.get(reverse('task_update', args=[task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/task_update.html')

        status = Status.objects.first()
        user = get_user_model().objects.first()
        task_data_update = {
            'name': 'new_name',
            'description': 'describe for new_name',
            'status': status.pk,
            'executor': user.pk,
        }
        response = self.client.post(reverse('task_update', args=[task.pk]), data=task_data_update)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks_list'))

        task_update = Task.objects.first()
        self.assertEqual(task_update.name, 'new_name')

    def test_task_delete_author(self):
        task = Task.objects.first()
        response = self.client.get(reverse('task_delete', args=[task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/task_delete.html')

        response = self.client.post(reverse('task_delete', args=[task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks_list'))
        self.assertEqual(Task.objects.count(), 0)

    def test_task_delete_not_author(self):
        user_not_author = get_user_model().objects.create(
            password="password_test",
            username="not_author",
            first_name="first_name_test2",
            last_name="last_name_test2",
        )
        self.client.force_login(user_not_author)
        task = Task.objects.first()
        response = self.client.get(reverse('task_delete', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('task_delete', args=[task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks_list'))
        self.assertEqual(Task.objects.count(), 1)

