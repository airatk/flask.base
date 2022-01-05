from app.models.user import User


def create_tables_if_not_exists():
    User.create_table()
