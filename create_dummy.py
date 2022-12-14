"""
 Copyright 2022 Google LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 """

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
