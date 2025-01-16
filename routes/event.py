"""
Defines the blueprint for the events
"""
from flask import Blueprint
from flask_restful import Api

from resources import EventResource, GetEventResource

EVENT_BLUEPRINT = Blueprint("event", __name__)

Api(EVENT_BLUEPRINT).add_resource(
    EventResource, "/event/"
)
# Api(EVENT_BLUEPRINT).add_resource(
#     GetEventResource, "/event/<string:key>"
# )
