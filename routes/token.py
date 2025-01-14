"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import TokenResource

TOKEN_BLUEPRINT = Blueprint("token", __name__)
Api(TOKEN_BLUEPRINT).add_resource(
    TokenResource, "/token/")
