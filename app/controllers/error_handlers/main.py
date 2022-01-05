from flask import jsonify

from werkzeug.exceptions import Forbidden
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import MethodNotAllowed
from werkzeug.exceptions import InternalServerError


def forbidden(_: Forbidden):
    return (jsonify(message="У вас нет доступа к этой странице."), 403)

def not_found(_: NotFound):
    return (jsonify(message="Неверный путь. Обратитесь к разработчику."), 404)

def method_not_allowed(_: MethodNotAllowed):
    return (jsonify(message="Неверный http-метод. Обратитесь к разработчику."), 405)

def internal_server_error(_: InternalServerError):
    return (jsonify(message="Ошибка выполенения. Обратитесь к разработчику."), 500)
