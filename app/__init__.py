from flask import Flask

from app.controllers import forbidden
from app.controllers import not_found
from app.controllers import method_not_allowed
from app.controllers import internal_server_error

from app.controllers import controller

from app.utilities.database.helpers import create_tables_if_not_exists


# Setting up database
create_tables_if_not_exists()

# Setting up the app itself
app: Flask = Flask(import_name=__name__)

app.register_error_handler(403, forbidden)
app.register_error_handler(404, not_found)
app.register_error_handler(405, method_not_allowed)
app.register_error_handler(500, internal_server_error)

app.register_blueprint(controller)
