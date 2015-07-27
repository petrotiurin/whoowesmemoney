from flask import Flask, request
from google.appengine.api import users
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/', methods=['GET', 'DELETE', 'PUT'])
def hello():
	if request.method == 'GET':
		return 'GET received'
	elif request.method == 'PUT':
		return 'PUT received'
	elif request.method == 'DELETE':
		return 'DELETE received'

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404