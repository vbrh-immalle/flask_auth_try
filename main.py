from flask import Flask

from flask_azure_oauth import FlaskAzureOauth

app = Flask(__name__)

app.config['AZURE_OAUTH_TENANCY'] = 'xxx'
app.config['AZURE_OAUTH_APPLICATION_ID'] = 'xxx'
app.config['AZURE_OAUTH_CLIENT_APPLICATION_IDS'] = ['xxx']

auth = FlaskAzureOauth()
auth.init_app(app=app)

@app.route('/unprotected')
def unprotected():
    return 'hello world'

@app.route('/protected')
@auth()
def protected():
    return 'hello authenticated entity'

@app.route('/protected-with-single-scope')
@auth('required-scope')
def protected_with_scope():
    return 'hello authenticated and authorised entity'

@app.route('/protected-with-multiple-scopes')
@auth('required-scope1 required-scope2')
def protected_with_multiple_scopes():
    return 'hello authenticated and authorised entity'
    