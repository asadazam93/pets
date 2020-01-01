from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.views import status


class ExtendedAPITestCase(APITestCase):

    def assert_bad_request(self, response):
        self.assertTrue(
            str(response.status_code).startswith("4"),
            "Status code is {}".format(response.status_code),
        )

    def assert_good_request(self, response):
        self.assertTrue(
            str(response.status_code).startswith("2"),
            "Status code is {}".format(response.status_code),
        )

    def authenticate_user(self, username):
        user = User.objects.get(username=username)
        self.client.force_authenticate(user=user)
        return user