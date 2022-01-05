from peewee import PostgresqlDatabase
from peewee import Model

from app.utilities.database.constants import DATABASE


class BaseModel(Model):
    class Meta:
        database: PostgresqlDatabase = DATABASE
        legacy_table_names: bool = False
