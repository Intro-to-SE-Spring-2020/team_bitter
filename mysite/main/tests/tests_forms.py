from django.test import TestCase
from main.forms import NewUserForm, AddFriendForm, DeleteFriendForm, BlockFriendForm, UnBlockFriendForm
from django.contrib.auth.forms import AuthenticationForm	
from main.models import Tweet	
from main.forms import TweetForm	
from django.urls import reverse	

# Create your tests here.	

class TweetFormTest(TestCase):	
	
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

class AddFriendFormTest(TestCase):
	def test_AddFriendForm_valid_data(self):
		form = AddFriendForm(data={'friendWaitToAdd': 'AddFriendForm'}) 
		self.assertTrue(form.is_valid())
	def test_AddFriendForm_no_data(self):
		form = AddFriendForm(data={})
		self.assertFalse(form.is_valid())
		
class DeleteFriendFormTest(TestCase):
	def test_DeleteFriendForm_valid_data(self):
		form = DeleteFriendForm(data={'friendWaitToDelete': 'DeleteFriendForm'}) 
		self.assertTrue(form.is_valid())
	def test_DeleteFriendForm_no_data(self):
		form = DeleteFriendForm(data={})
		self.assertFalse(form.is_valid())
		
class BlockFriendFormTest(TestCase):
	def test_BlockFriendForm_valid_data(self):
		form =BlockFriendForm(data={'friendWaitToDelete': 'BlockFriendForm'}) 
		self.assertFalse(form.is_valid())
	def test_BlockFriendForm_no_data(self):
		form = BlockFriendForm(data={})
		self.assertFalse(form.is_valid())
		
class UnBlockFriendFormTest(TestCase):
	def test_UnBlockFriendForm_valid_data(self):
		form =UnBlockFriendForm(data={'friendWaitToUnblock': 'BlockFriendForm'}) 
		self.assertFalse(form.is_valid())
	def test_UnBlockFriendForm_no_data(self):
		form = UnBlockFriendForm(data={})
		self.assertFalse(form.is_valid())
		
		
