from peewee import PostgresqlDatabase


DATABASE_NAME: str = "app_db"
DATABASE: PostgresqlDatabase = PostgresqlDatabase(database=DATABASE_NAME)
