from django.test import TestCase
from django.urls import reverse
from dotenv import load_dotenv
import os

# Create your tests here.


class SimpleTestViews(TestCase):

    def setUp(self):
        publicViews = ["index", "login", "register"]
        loggedOnlyViews = ["logout", "edit_profile", "view_profile", "change_password"]
        self.publicUrls = list()
        self.loggedUrls = list()
        for views in publicViews:
            self.publicUrls.append(reverse(views))
        for views in loggedOnlyViews:
            self.loggedUrls.append(reverse(views))

    def testPublicUrlWorks_withoutBeingLoged(self):
        for url in self.publicUrls:
            resp = self.client.get(url)
            self.assertEqual(resp.status_code, 200, "URL " + url + " returned not 200 error code but should be accessible for visitors")

    def testLoggedOnlyUrlDontWorks_withoutBeingLoged(self):
        for url in self.loggedUrls:
            resp = self.client.get(url)
            self.assertNotEqual(resp.status_code, 200, "URL " + url + " returned 200 code but should not be accessible when not logged in")
