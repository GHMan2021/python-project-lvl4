from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Status


class StatusTestCase(TestCase):

    fixtures = ['user.json', 'status.json']

    def setUp(self):
        user_logged = get_user_model().objects.first()
        self.client.force_login(user_logged)

    def test_statuses_list(self):
        response = self.client.get(reverse('statuses_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='statuses/statuses_list.html')

    def test_status_create(self):
        response = self.client.get(reverse('status_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='statuses/status_create.html')

        status_create = {
            'name': 'name_test1'
        }
        response = self.client.post(reverse('status_create'), data=status_create)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('statuses_list'))

        status = Status.objects.last()
        self.assertEqual(status.name, 'name_test1')
        self.assertEqual(Status.objects.count(), 2)

    def test_status_update(self):
        status_test = Status.objects.first()
        response = self.client.get(reverse('status_update', args=[status_test.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='statuses/status_update.html')

        new_name = 'new_name_test'
        response = self.client.post(reverse('status_update', args=[status_test.pk]), {'name':new_name})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('statuses_list'))

        status_update = Status.objects.first()
        self.assertEqual(status_update.name, 'new_name_test')

    def test_status_delete(self):
        status_test = Status.objects.first()
        response = self.client.get(reverse('status_delete', args=[status_test.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='statuses/status_delete.html')

        response = self.client.post(reverse('status_delete', args=[status_test.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('statuses_list'))
        self.assertEqual(Status.objects.count(), 0)
