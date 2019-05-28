from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from pointsEau.models import PointEau
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


class PointEauAPITest(APITestCase, TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@gmail.com', password='12345')
        login = self.client.force_login(self.user)
        self.pe = PointEau.objects.create(nom="point trois", lat=34.12345678, long=22.12345678, desc="A test point eau", owner=self.user)
        self.urlList = reverse('pointeau-list')
        self.urlDetail = reverse('pointeau-detail', kwargs={'pk': self.pe.id})
        self.data = {
            "nom": "Point eau test api",
            "lat": "43.1235678",
            "long": "34.12345678",
            "desc": "Point eau 1",
            "owner": self.user.id
        }

    def test_create_pointeau(self):
        response = self.client.post(self.urlList, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PointEau.objects.count(), 2)

    def test_delete(self):
        response = self.client.delete(self.urlDetail, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieval_pointeau(self):
        response = self.client.get(self.urlDetail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Tests on object
        parsed = response.json()
        self.assertEqual(parsed['nom'], "point trois")
        self.assertEqual(float(parsed['lat']), 34.12345678)
        self.assertEqual(float(parsed['long']), 22.12345678)
        self.assertEqual(parsed['desc'], "A test point eau")
        self.assertEqual(parsed['owner'], self.user.username)

    def test_notLoggedInPost(self):
        self.client.logout()
        response = self.client.post(self.urlDetail, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_pointeau(self):
        response = self.client.get(self.urlDetail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        parsed = response.json()
        previousLat = float(parsed['lat'])

        # Temporary change
        self.data['lat'] = "45.4"
        response = self.client.put(self.urlDetail, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        parsedAfter = response.json()
        self.assertNotEqual(float(45.4), float(previousLat))
        self.data['lat'] = previousLat

    def test_notOwner_pointeau(self):
        response = self.client.get(self.urlDetail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        userT = User.objects.create_user(username='meanUser', email='imMean@gmail.com', password='12345')
        login = self.client.force_login(userT)

        # Test on update
        response = self.client.put(self.urlDetail, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Test on create
        response = self.client.post(self.urlDetail, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # Test on delete
        response = self.client.delete(self.urlDetail, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
