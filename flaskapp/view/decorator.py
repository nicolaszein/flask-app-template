import json

from functools import wraps
from flask import request, jsonify, g
from marshmallow import EXCLUDE


def validate_request_body(schema):
    def wrapper(function):
        @wraps(function)
        def wrapped(*args, **kwargs):
            try:
                data = json.loads(request.data) if request.data else {}
            except ValueError:
                return jsonify(code="BAD_REQUEST", message='Invalid request body'), 400

            g.valid_request_body = schema.load(data, unknown=EXCLUDE)
            return function(*args, **kwargs)
        return wrapped
    return wrapper


def validate_query_params(schema):
    def wrapper(function):
        @wraps(function)
        def wrapped(*args, **kwargs):
            schema.load(request.args.to_dict(), unknown=EXCLUDE)

            return function(*args, **kwargs)
        return wrapped
    return wrapper
