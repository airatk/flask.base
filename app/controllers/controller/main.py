from typing import Dict

from flask import jsonify

from app.models.user import User

from app.utilities.checks.user import check_user_authorisation


@check_user_authorisation
def method(user: User, **method_data):
    result: Dict = { "user_id": user.id, "method_data_length": len(method_data) }

    return (jsonify(message=f"Сообщение об успешном выполнении запроса", result=result), 200)
