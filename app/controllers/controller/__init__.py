from flask import Blueprint

from app.controllers.controller.main import method


controller: Blueprint = Blueprint(name=__name__.split(".")[-1], import_name=__name__, url_prefix="/<string:token>/controller-path")

controller.add_url_rule(rule="/method-path", endpoint="method", view_func=method, methods=[ "GET", "POST" ])
