from flask import Flask

app = Flask(__name__)
app.secret_key = 'my-super-secret-phrase-I-dont-tell-this-to-nobody-because-it-is-secure-to-be-silent'

from views import *