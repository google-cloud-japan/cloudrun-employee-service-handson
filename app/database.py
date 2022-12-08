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

from os import environ

from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

projectid = environ.get("PROJECT_ID")
instanceid = environ.get("INSTANCE_ID")
unix_socket_name = "/cloudsql/{}:asia-northeast1:{}".format(projectid, instanceid)

engine = create_engine(
    engine.url.URL.create(
        drivername="mysql+pymysql",
        username=environ.get("DB_USER_NAME"),
        password=environ.get("DB_USER_PASSWORD"),
        database=environ.get("DATABASE_ID"),
        query={"unix_socket": unix_socket_name},
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,
    pool_recycle=1800,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
