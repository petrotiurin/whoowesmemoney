from flask import Flask, request
from google.appengine.api import users
from google.appengine.ext import ndb
app = Flask(__name__)
app.config['DEBUG'] = True


# Note: We don't need to call run() since our application is 
# embedded within the App Engine WSGI application server.

DEFAULT_DB_NAME = 'default_db'

def db_key(db_name=DEFAULT_DB_NAME):
    # We use db_name as the key.
    return ndb.Key('DB', db_name)

class Entry(ndb.Model):
    # A main model for representing an individual entry.
    content = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

@app.route('/', methods=['GET', 'DELETE', 'POST'])
def hello():
    if request.method == 'GET':
        return 'GET received'
    elif request.method == 'POST':
        # To send dummy POST request set content length to 0
        db_name = request.args.get('db_name',
                                    DEFAULT_DB_NAME)
        entry = Entry(parent=db_key(db_name))
        entry.content = "potato"
        entry.put()
        return entry.content
    elif request.method == 'DELETE':
        return 'DELETE received'

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404