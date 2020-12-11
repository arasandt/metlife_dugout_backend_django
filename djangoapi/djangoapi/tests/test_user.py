import pytest
from userprofile.models import UserProfile

# from django.contrib.auth.models import User

@pytest.fixture
def get_user():
    return {"email": "arasandt@gmail.com",
    "password": "a",
    "firstName": "Sample",
    "lastName": "Person",
    "id" : 128537
    }

@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()

def display_result(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'\t{func.__name__}.. ok')
    return inner

@pytest.mark.django_db()
def test010_userprofile(api_client, get_user):

    @display_result
    def create_userprofile_with_id():
        input_user = get_user
        response = api_client.post('/api/signup', input_user, format='json')
        [input_user.pop(key) for key in ['password']]
        output_user = dict(response.data['data'][0])
        [output_user.pop(key) for key in ['token', 'rank', 'coins']]
        assert response.status_code == 201
        assert input_user == output_user

    @display_result
    def query_userprofile_with_id():
        input_user = get_user['id']
        response = api_client.get(f'/api/userprofile/?id={input_user}')
        # print(response.data)
        assert response.status_code == 200

    @display_result
    def update_userprofile_with_id():
        input_user = get_user['id']
        upd = {'firstName' : 'Arasan'}
        response = api_client.put(f'/api/userprofile/?id={input_user}', data=upd, format='json')
        assert response.data['data']['firstName'] == upd['firstName']
        
    @display_result
    def delete_userprofile_with_id():
        input_user = get_user['id']
        # import pdb; pdb.set_trace()
        response = api_client.delete(f'/api/userprofile/?id={input_user}')
        assert response.status_code == 200

    create_userprofile_with_id()
    query_userprofile_with_id()
    update_userprofile_with_id()
    delete_userprofile_with_id()
