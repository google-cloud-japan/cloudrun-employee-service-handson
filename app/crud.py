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

from sqlalchemy.orm import Session
from app import models, schemas


def get_users(db: Session):
    return db.query(models.User).all()


def get_user(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def create_user(db: Session, user: schemas.UserBase):
    db_user = models.User(name=user.name, mail=user.mail)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, id: int, user: schemas.UserBase):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if db_user is None:
        return None
    db_user.name = user.name
    db_user.mail = user.mail
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_users(db: Session):
    db.query(models.User).delete()
    db.commit()
    return


def delete_user(db: Session, id: int):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
