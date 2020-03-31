



from django.test import TestCase
from main.forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm




















class TestForms(TestCase):

	def test_new_user_form_valid_data(self):
		form = NewUserForm(data={
			'username': 'newuser',
			'first_name': 'John',
			'last_name': 'Smith',
			'email': 'abc@gmail.com',
			'password1': 'Abc123*sample',
			'password2': 'Abc123*sample'
			}) 
		self.assertTrue(form.is_valid())

	def test_new_user_forms_no_data(self):
		form = NewUserForm(data={})
		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors),6)



	def test_authenticate_forms_no_data(self):
		n_form = AuthenticationForm(data={})
		self.assertFalse(n_form.is_valid())
		self.assertEquals(len(n_form.errors),2)


