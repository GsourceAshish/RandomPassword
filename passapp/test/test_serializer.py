from rest_framework import status
from rest_framework.test import APITestCase

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data={
            "email":"he@gmail.com",
            "first_name":"hello",
            "last_name":"bye"
           
        }
        response=self.client.post('http://127.0.0.1:8000/rest/',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


class ChangePasswordTestCase(APITestCase):
    def test_changepassword(self):
        data={
            
            "old_password":"test123",
            "new_password":"1234test",
            "confirm_password":"1234test"
        }
        response=self.client.post('http://127.0.0.1:8000/api/change_password/',data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)