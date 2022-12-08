from faker import Faker
import requests
from sys import argv

fake = Faker()
n = int(argv[1])
url = argv[2]


def create_user():
    user = {}
    user["name"] = fake.first_name()
    user["mail"] = fake.email()
    return user


def make_requests(url, user):
    r = requests.post(url, json=user)
    return r


for i in range(n):
    user = create_user()
    r = make_requests(url, user)
    print("status_code:" + str(r.status_code) + ", created:" + r.text)
