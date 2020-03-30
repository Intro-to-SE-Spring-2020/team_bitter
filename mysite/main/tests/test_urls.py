from django.test import SimpleTestCase
from django.urls import reverse, resolve, path
from main.views import homepage, register, login_request, logout_request
import json

# Create your tests here.

class TestUrls(SimpleTestCase):

	def test_homepage_url_is_resolved(self):
		url = reverse('main:homepage')
		self.assertEquals(resolve(url).func,homepage)



		