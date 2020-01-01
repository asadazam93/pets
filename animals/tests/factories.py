import factory
import datetime

from django.contrib.auth.models import User
from factory.fuzzy import FuzzyDateTime, FuzzyText
from pytz import UTC

from animals.models import Cat, Dog

USER_PASSWORD = 'test1234'

def add_m2m_data(m2m_relation, data):
    """ Helper function to enable factories to easily associate many-to-many data with created objects. """
    if data:
        m2m_relation.add(*data)


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user_%d' % n)
    password = factory.PostGenerationMethodCall('set_password', USER_PASSWORD)
    is_active = True
    is_superuser = False
    is_staff = False
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = User

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if create:
            add_m2m_data(self.groups, extracted)


class CatFactory(factory.DjangoModelFactory):
    name = FuzzyText()
    birthday = FuzzyDateTime(datetime.datetime(2018, 1, 1, tzinfo=UTC))

    class Meta:
        model = Cat


class DogFactory(factory.DjangoModelFactory):
    name = FuzzyText()
    birthday = FuzzyDateTime(datetime.datetime(2018, 1, 1, tzinfo=UTC))

    class Meta:
        model = Dog