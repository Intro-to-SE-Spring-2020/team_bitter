from django.test import SimpleTestCase
from django.urls import reverse, resolve, path
from main.views import homepage, register, login_request, logout_request
import json

# Create your tests here.

class TestUrls(SimpleTestCase):

	def test_homepage_url_is_resolved(self):
		url = reverse('main:homepage')
		self.assertEquals(resolve(url).func,homepage)
		
	def test_login_url_is_resolved(self):
		url = reverse('main:login')
		self.assertEquals(resolve(url).func,login_request)

	def test_logout_url_is_resolved(self):
		url = reverse('main:logout')
		self.assertEquals(resolve(url).func,logout_request)

	def test_register_url_is_resolved(self):
		url = reverse('main:register')
		self.assertEquals(resolve(url).func,register)



		
