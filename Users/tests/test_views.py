from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from Places.models import Places
from Users.models import User,Leader
from Places.api.views import UniquePlaceAPI
from rest_framework.test import APIRequestFactory
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet 


factory = APIRequestFactory()


class ViewTestCase(TestCase):
    def test_post_creation(self):
        c = Client()  
        response = c.post('http://127.0.0.1:8000/api/User/sign-up/',{'username': 'john','email':'john@gmail.com', 'password': 'smith','first_name':'johny','last_name' :'depp'})
        self.assertEqual(response.status_code, 400)