from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Label


class LabelTestCase(TestCase):

    fixtures = ['user.json', 'label.json']

    def setUp(self):
        user_logged = get_user_model().objects.first()
        self.client.force_login(user_logged)

    def test_labels_list(self):
        response = self.client.get(reverse('labels_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='labels/labels_list.html')

    def test_label_create(self):
        response = self.client.get(reverse('label_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='labels/label_create.html')

        label_create = {
            'name': 'name_test1'
        }
        response = self.client.post(reverse('label_create'), data=label_create)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('labels_list'))

        status = Label.objects.last()
        self.assertEqual(status.name, 'name_test1')
        self.assertEqual(Label.objects.count(), 2)

    def test_label_update(self):
        label_test = Label.objects.first()
        response = self.client.get(reverse('label_update', args=[label_test.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='labels/label_update.html')

        new_name = 'new_name_test'
        response = self.client.post(reverse('label_update', args=[label_test.pk]), {'name':new_name})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('labels_list'))

        label_update = Label.objects.first()
        self.assertEqual(label_update.name, 'new_name_test')

    def test_label_delete(self):
        label_test = Label.objects.first()
        response = self.client.get(reverse('label_delete', args=[label_test.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='labels/label_delete.html')

        response = self.client.post(reverse('label_delete', args=[label_test.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('labels_list'))
        self.assertEqual(Label.objects.count(), 0)
