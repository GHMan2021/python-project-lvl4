from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import CustomUser


class CustomUserTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(
            first_name='user1_first_name',
            last_name='user1_last_name',
            username='user1_username',
            password='123qweASD',
            )
        self.client.login(username=user1.username, password="123qweASD")

    def test_user(self):
        user1 = CustomUser.objects.get(pk=1)
        self.assertEqual(user1.first_name, 'user1_first_name')
        self.assertEqual(user1.last_name, 'user1_last_name')
        self.assertEqual(user1.username, 'user1_username')

    def test_users_list(self):
        response = self.client.get(reverse('users_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/users_list.html')

    def test_user_add(self):
        response = self.client.get(reverse('user_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/user_add.html')

        user2 = {
            'first_name': 'user2_first_name',
            'last_name': 'user2_last_name',
            'username': 'user2_username',
            'password1': 'Nx7sDQ9D',
            'password2': 'Nx7sDQ9D',
        }
        response = self.client.post(reverse('user_add'), user2)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('/'))

        user = get_user_model().objects.get(username=user2['username'])
        self.assertEqual(user.username, 'user2_username')

    def test_user_update(self):
        user1 = get_user_model().objects.first()
        response = self.client.get(reverse('user_update', args=[user1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/user_update.html')

        user3 = {
            'first_name': 'user3_first_name',
            'last_name': 'user3_last_name',
            'username': 'user3_username',
            'password1': 'Nx7sDQ9D3',
            'password2': 'Nx7sDQ9D3',
        }

        response = self.client.post(reverse('user_update', args=[user1.pk]), user3)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('/'))

        user1_update = get_user_model().objects.first()
        self.assertEqual(user1_update.first_name, 'user3_first_name')
        self.assertTrue(user1_update.check_password('Nx7sDQ9D3'))

    def test_user_delete(self):
        user = get_user_model().objects.first()
        response = self.client.get(reverse('user_delete', args=[user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/user_delete.html')

        response = self.client.post(reverse('user_delete', args=[user.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.count(), 0)
