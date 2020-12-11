# run as python manage.py test

from rest_framework.test import APITestCase, force_authenticate, APIClient, APITransactionTestCase 
import json
from django.test import TestCase

def display_result(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'\t{func.__name__}.. ok')
    return inner

# class MainTest(APITransactionTestCase ):
class MainTest(TestCase):
    user = {
        "email": "arasandt@gmail.com",
        "password": "a",
        "firstName": "Sample",
        "lastName": "Person",
        "id" : 128537,
   }
        
    # @classmethod
    # def setUpClass(cls):
    #     cls.client = APIClient()
    #     print("\nUserprofile Endpoints by creating a new id")

    # @classmethod
    # def tearDownClass(cls):
    #     pass
    #     # print("Tearing down Class....")    

    def setUp(self):
        self.client = APIClient()
        pass
        # print(" Setting up...")

    def tearDown(self):
        pass
        # print(" Tearing down....")    

    def test010_userprofile(self):

        @display_result
        def create_userprofile_with_id():
            response = self.client.post('/api/signup', self.user, format='json')
            input_user = self.user
            [input_user.pop(key) for key in ['password']]
            output_user = dict(response.data['data'][0])
            [output_user.pop(key) for key in ['token', 'rank', 'coins']]
            self.assertEqual(response.status_code, 201)
            self.assertEqual(input_user, output_user)
        
        @display_result
        def query_userprofile_with_id():
            response = self.client.get(f'/api/userprofile/?id={self.user["id"]}')
            self.assertEqual(response.status_code, 200)

        @display_result
        def update_userprofile_with_id():
            upd = {'firstName' : 'Arasan'}
            response = self.client.put(f'/api/userprofile/?id={self.user["id"]}', data=upd, format='json')
            # print(response.data['data']['firstName'])
            self.assertEqual(response.data['data']['firstName'], upd['firstName'])
        
        @display_result
        def delete_userprofile_with_id():
            # import pdb; pdb.set_trace()
            response = self.client.delete(f'/api/userprofile/?id={self.user["id"]}')
            self.assertEqual(response.status_code, 200)

        create_userprofile_with_id()
        query_userprofile_with_id()
        update_userprofile_with_id()
        delete_userprofile_with_id()


