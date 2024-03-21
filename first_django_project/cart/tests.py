from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
def add(a,b):
    return a+b
        

class UserTest(TestCase):


    def test_add(self):      #test_ must be compoulsary
         self.assertEqual(add(5,5),10)     
        #assertEqual compares expected value with actual value
         
    def setUp(self):
        self.user = User.objects.create(username="TestUser",
                            first_name="TestFirstName",
                            last_name="TestLastName",
                            email="TestEmail@123",
                            password="User@123",
                            )
    def test_create_user(self):
        user = User.objects.get(username="TestUser")
        self.assertEqual(user.username,self.user.username)

    def test_update_user(self):
        user = User.objects.get(username="TestUser")
        old_email=user.email
        user.email="updated.email@gmail.com"
        user.save()

        user = User.objects.get(username="TestUser")
        self.assertNotEqual(old_email,user.email)


