from flask import Flask, request
from functools import wraps

app = Flask(__name__)

# Decorator for basic authentication
def basic_auth_required(username, password):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth or auth.username != username or auth.password != password:
                return 'Unauthorized', 401
            return f(*args, **kwargs)
        return decorated
    return decorator

@app.route('/token')
@basic_auth_required('admin', 'password')  # Change username and password as needed
def token_endpoint():
    return 'Authenticated and authorized'

if __name__ == '__main__':
    app.run()