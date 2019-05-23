from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse 
from pointsEau.models import PointEau
from django.test import TestCase
from django.contrib.auth.models import User


class PointEauAPITest(APITestCase, TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser',email='test@gmail.com' ,password='12345')
        login = self.client.force_login(self.user)
        self.pe = PointEau.objects.create(nom="point trois", lat=34.12345678, long=22.12345678, desc="A test point eau", owner=self.user)

    def test_create_pointeau(self):
        url = reverse('pointeau-list')
        data = {
            "nom": "Point eau test api",
            "lat": "43.1235678",
            "long": "34.12345678",
            "desc": "Point eau 1",
            "owner" : self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PointEau.objects.count(), 2)

    def test_retrieval_pointeau(self):
        response = self.client.get(reverse('pointeau-detail', kwargs={'pk': self.pe.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Tests on object
        parsed = response.json()
        self.assertEqual(parsed['nom'], "point trois")
        self.assertEqual(float(parsed['lat']), 34.12345678)
        self.assertEqual(float(parsed['long']), 22.12345678 )
        self.assertEqual(parsed['desc'], "A test point eau")
        self.assertEqual(parsed['owner'], self.user.username)