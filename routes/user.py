"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import UserResource, GetUserResource

USER_BLUEPRINT = Blueprint("user1", __name__)
Api(USER_BLUEPRINT).add_resource(
    UserResource, "/user/"
)
Api(USER_BLUEPRINT).add_resource(
    GetUserResource, "/user/<string:key>"
)