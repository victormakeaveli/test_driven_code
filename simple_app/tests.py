import unittest
from django.test import Client
from django.urls import reverse


class testing_app(unittest.TestCase):

    def test_simple(self):    
    
        #assume
        client = Client()
        response = client.get(reverse('index'))
    
        #action
        result = response.status_code
    
        #assert
        self.assertEquals(result, 200)