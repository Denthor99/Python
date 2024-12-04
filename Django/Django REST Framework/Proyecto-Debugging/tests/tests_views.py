import json
from django.test import TestCase
from django.urls import reverse

class UserViewSetTest(TestCase):
    fixtures = ['user']

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_for_user_exists_at_desired_location(self):
        response = self.client.get('/users/1')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_accept_post(self):
        user = {"username": "admin123", "password": "admin123"}
        response = self.client.post('/users/', json.dumps(user), content_type='application/json')
        print(response.content)
        self.assertEqual(response.status_code, 201)
    
    def test_view_url_exists_at_desired_location_home(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')