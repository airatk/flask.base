from peewee import AutoField

from app.utilities.database.base_model import BaseModel


class User(BaseModel):
    id: AutoField = AutoField()
