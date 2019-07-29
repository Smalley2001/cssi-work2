import webapp2
import jinja2
import os

from myMemes import MemeInfo
from google.appengine.api import urlfetch
import json
#This initializes the jinja2 environment
#This is the same for almost every app you build
#This is a constructor
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions= ["jinja2.ext.autoescape"],
    autoescape= True
