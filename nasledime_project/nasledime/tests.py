from django.contrib.auth import get_user_model
from django.http import request
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.test.client import Client

from nasledime_project.nasledime.models import Will

User = get_user_model()


class WillsTestCase(TestCase):
    def setUp(self):
        user = User(email="testemail@abv.bg")
        user.set_password('MyTestPassword4321')
        user.save()
        self.client.login(email='testemail@abv.bg', password='MyTestPassword4321')

    def test_create_will(self):
        data = {
            'id': 1,
            'first_name': "Somefirstname",
            'last_name': "Somelastname",
            'address': "Some address",
            'uic': "45657474",
            'text': "This is my will's text",
            'user_id': 1,
        }
        url_response = self.client.post(reverse('create will'), kwargs=data)
        self.assertEqual(url_response.status_code, 200)
        # will = Will.objects.last()
        # will.refresh_from_db()
        # self.assertEqual(will.last_name, 'Somelastname')

    def test_will_details(self):
        Will.objects.create(
            first_name="Somefirstname",
            last_name="Somelastname",
            uic="45657474",
            text="This is my will's text",
            address='Some address',
            user_id=1,
        )

        url = reverse('will details', args=[1])
        self.response = self.client.get(url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'This is my')
        self.assertContains(self.response, 'Аз, долуподписаният/та,')

    def test_edit_will(self):
        will = Will.objects.create(
            first_name="Somefirstname",
            last_name="Somelastname",
            uic="45657474",
            text="This is my will's text",
            address='Some address',
            user_id=1,
        )
        response = self.client.post(
            reverse('edit will', kwargs={'pk': will.id}),
                      {'first_name': "SomeNewfirstname",
                       'last_name': "SomeNewlastname",
                       'uic': "45657474",
                       'text': "This is my will's text",
                       'address': "Some address",
                       'user_id': 1,})
        self.assertEqual(response.status_code, 302)
        will.refresh_from_db()
        self.assertEqual(will.last_name, "SomeNewlastname")

    def test_delete_get_request(self):
        will = Will.objects.create(
            first_name="Somefirstname",
            last_name="Somelastname",
            uic="45657474",
            text="This is my will's text",
            address='Some address',
            user_id=1,
        )
        response = self.client.get(reverse('delete will', args=(will.id,)), follow=True)
        self.assertContains(response, 'Сигурни ли сте, че искате да изтриете завещанието?')

    def test_delete_post_request(self):
        will = Will.objects.create(
            first_name="Somefirstname",
            last_name="Somelastname",
            uic="45657474",
            text="This is my will's text",
            address='Some address',
            user_id=1,
        )
        post_response = self.client.post(reverse_lazy('delete will', args=(will.id,)), follow=True)
        self.assertRedirects(post_response, reverse_lazy('wills list'), status_code=302)