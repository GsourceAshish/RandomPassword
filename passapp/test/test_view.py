from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from passapp.models import CustomUser


class TestApi(APITestCase):

    def setUp(self):
        self.headerInfo = {'content-type': 'application/json'}
        # example of query to be used on URL.
        self.user = CustomUser.objects.create(
           email = 'any@gmail.com',
           first_name='anyyy',
           last_name='testname',
       )
        self.user.save()
   
       # payload to be used to test PUT method for example...
        self.user_data = {
           'email': 'othername@gmail.com',
           'first_name': 'ass',
           'last_name': 'othertestname'
       }

       # again: In the example used in the question the app_name is 'passapp'
       # that's why reverse('passapp:rest-list')...
        self.url_user_list = reverse('passapp:rest-list')
        
    """
    Test User endpont.
    """
    def test_get_user(self):
        """GET method"""
        response = self.client.get(self.url_user_list, 
        self.user_data, 
        format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """ test POST method for User endpoint"""
        response = self.client.post(
            self.url_user_list, self.user_data,
            headers=self.headerInfo,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

