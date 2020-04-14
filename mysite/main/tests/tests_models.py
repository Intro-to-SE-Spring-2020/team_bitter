from django.test import TestCase
from main.models import Tweet 
from main.models import UserRelationship, UserBlocked

# Create your tests here.

class UserRelationshipModelTest(TestCase):

    def setUp(self):
        UserRelationship.objects.create(selfname='selfnameForTest',friendname='friendnameForTest')

    def test_UserRelationship(self):
        userRelationship= UserRelationship.objects.get(id=1)
        field_label =userRelationship._meta.get_field('friendname').verbose_name
        self.assertEquals(field_label, 'friendname')
    
class UserBlockedModelTest(TestCase):

    def setUp(self):
        UserBlocked.objects.create(selfname='selfnameForTest',blockname='blockednameForTest')
    def test_UserBlocked(self):
        userBlocked= UserBlocked.objects.get(id=1)
        field_label =userBlocked._meta.get_field('blockname').verbose_name
        self.assertEquals(field_label, 'blockname')
