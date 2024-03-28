from flask import request, jsonify
from functools import wraps
import jwt
from config.config import PUBLIC_KEY


def jwt_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            token_parts = token.split()
            if len(token_parts) != 2:
                return jsonify({'message': 'Invalid token format'}), 401

            token = token_parts[1]
            data = jwt.decode(token, PUBLIC_KEY, algorithms=['RS256'])
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return func(*args, **kwargs)

    return decorated
