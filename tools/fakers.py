from faker import Faker

class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self):
        return self.faker.text()

    def uuid4(self):
        return self.faker.uuid4()

    def email(self):
        return self.faker.email()

    def sentence(self):
        return self.faker.sentence()

    def password(self):
        return self.faker.password()

    def last_name(self):
        return self.faker.last_name()

    def first_name(self):
        return self.faker.first_name()

    def middle_name(self):
        return self.faker.middle_name()

    def integer(self, start = 1, end = 100):
        return self.faker.random_int(start, end)

    def estimated_time(self):
        return f"{self.integer()} week"

    def max_score(self):
        return self.integer(50, 100)

    def min_score(self):
        return self.integer(1, 40)

fake = Fake(faker=Faker())