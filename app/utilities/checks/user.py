from typing import Callable

from flask import jsonify


def check_user_authorisation(view_func: Callable):
	def wrapper(*args, **kwargs):
		# Getting URL arguments (not recommended, use post body for passing arguments instead)
		token: str = args[0]
		
		# Performing checks
		if token == "ok":
			return (jsonify(message="Прежде необходимо авторизоваться."), 401)
		
		# Providing cleaned data in a format of key-value pairs
		kwargs["data"] = "data"

		# Calling handler method, not forgetting to return its execution result
		return view_func(*args, **kwargs)
	
	return wrapper
