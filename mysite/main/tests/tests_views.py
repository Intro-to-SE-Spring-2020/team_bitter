from django.urls import reverse
from django.contrib.auth.models import User
from main.models import UserBlocked,UserBlocked
from datetime import datetime
import json

# Create your tests here.

class Tweet_Url_test(TestCase):

    def test_view_url_in_desired_location(self):
        response = self.client.get('/homepage/')
        self.assertEqual(response.status_code, 200)


    def test_view_url_by_name(self):
        response = self.client.get(reverse('main:homepage'))
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        response = self.client.get(reverse('main:homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')
    
    def test_register(self):
        client = Client()
        response = client.get(reverse('main:register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/register.html')

    def test_account(self):
        response = self.client.get(reverse('main:account'))
        self.assertEqual(response.status_code, 200)
