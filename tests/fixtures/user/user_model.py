from pytest_factoryboy import register

import factory.fuzzy

from models import UserProfile

from faker import Faker

faker = Faker()

@register(_name="user_profile")
class UserProfileFactory(factory.Factory):

    class Meta:
        model = UserProfile

    id = factory.LazyFunction(lambda: faker.random_int())
    username = factory.LazyFunction(lambda: faker.user_name())
    name = factory.LazyFunction(lambda: faker.name())
    email = factory.LazyFunction(lambda: faker.email())
    google_access_token = factory.LazyFunction(lambda: faker.sha256())
    yandex_access_token = factory.LazyFunction(lambda: faker.sha256())
