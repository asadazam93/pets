import datetime
import pytz

from animals.tests.test_utils import ExtendedAPITestCase
from animals.tests.factories import CatFactory, DogFactory, UserFactory
from django.urls import reverse


def load_data():
    data = dict()
    owner_one = UserFactory(username='owner_one')
    owner_two = UserFactory(username='owner_two')
    cat = CatFactory(owner=owner_one)
    dog = DogFactory(owner=owner_one)

    data['owner_one'] = owner_one
    data['owner_two'] = owner_two
    data['cat'] = cat
    data['dog'] = dog
    return data


class TestCatViewSet(ExtendedAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data = load_data()
        cls.birthday = datetime.datetime.now(tz=pytz.utc) - datetime.timedelta(days=600)

    def test_cat_create_success(self):
        user = self.authenticate_user('owner_one')
        response = self.client.post(
            reverse('animals:cats-list'),
            {
                'name': 'persian',
                'birthday': str(self.birthday.date()),
                'owner': user.id
            },
            format='json'
        )
        self.assert_good_request(response)

    def test_cat_list_success(self):
        self.authenticate_user('owner_one')
        response = self.client.get(
            reverse('animals:cats-list'),
            format='json'
        )
        self.assert_good_request(response)

    def test_cat_update_success(self):
        self.authenticate_user('owner_one')
        response = self.client.patch(
            reverse('animals:cats-detail', kwargs={'pk': self.data['cat'].id}),
            {
                'name': 'persian_updated'
            },
            format='json'
        )
        self.assert_good_request(response)

    def test_cat_update_failure(self):
        self.authenticate_user('owner_two')
        response = self.client.patch(
            reverse('animals:cats-detail', kwargs={'pk': self.data['cat'].id}),
            {
                'name': 'persian_updated'
            },
            format='json'
        )
        self.assert_bad_request(response)


    def test_cat_get_success(self):
        self.authenticate_user('owner_one')
        response = self.client.get(
            reverse('animals:cats-detail', kwargs={'pk': self.data['cat'].id}),
            format='json'
        )
        self.assert_good_request(response)


class TestDogViewSet(ExtendedAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data = load_data()
        cls.birthday = datetime.datetime.now(tz=pytz.utc) - datetime.timedelta(days=600)

    def test_dog_create_success(self):
        user = self.authenticate_user('owner_one')
        response = self.client.post(
            reverse('animals:dogs-list'),
            {
                'name': 'german',
                'birthday': str(self.birthday.date()),
                'owner': user.id
            },
            format='json'
        )
        self.assert_good_request(response)

    def test_dog_list_success(self):
        self.authenticate_user('owner_one')
        response = self.client.get(
            reverse('animals:dogs-list'),
            format='json'
        )
        self.assert_good_request(response)

    def test_dog_update_success(self):
        self.authenticate_user('owner_one')
        response = self.client.patch(
            reverse('animals:dogs-detail', kwargs={'pk': self.data['dog'].id}),
            {
                'name': 'german_updated'
            },
            format='json'
        )
        self.assert_good_request(response)

    def test_dog_update_failure(self):
        self.authenticate_user('owner_two')
        response = self.client.patch(
            reverse('animals:dogs-detail', kwargs={'pk': self.data['dog'].id}),
            {
                'name': 'german_updated'
            },
            format='json'
        )
        self.assert_bad_request(response)


    def test_dog_get_success(self):
        self.authenticate_user('owner_one')
        response = self.client.get(
            reverse('animals:dogs-detail', kwargs={'pk': self.data['dog'].id}),
            format='json'
        )
        self.assert_good_request(response)