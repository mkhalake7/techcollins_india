"""
Define the REST verbs relative to the events
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from repositories import EventRepository
from flask import make_response, request


def serialize_event(event):
    return {
        'id': event.id,
        'name': event.name,
        'date': event.date.strftime("%Y-%m-%d"),
        'start_time': event.start_time.strftime("%H:%M:%S"),
        'end_time': event.end_time.strftime("%H:%M:%S"),
        'venue': event.venue,
    }


class GetEventResource(Resource):
    """ Verbs relative to the events """

    @staticmethod
    @swag_from("../swagger/event/GET.yml")
    def get(key):
        """ Return an event key information based on its id or name """
        event = EventRepository.get(key=key)
        if event:
            return make_response(jsonify({"event": serialize_event(event)}), 200)
        else:
            return make_response(jsonify({"error": "Invalid event"}), 400)


class EventResource(Resource):
    """ Verbs relative to the events """

    @staticmethod
    @swag_from("../swagger/event/LIST.yml")
    def get():
        """ Return all the event information """
        events = EventRepository.list()
        return make_response(jsonify({"list_event": [serialize_event(event) for event in events]}), 200)

    @staticmethod
    @swag_from('../swagger/event/POST.yml')
    def post():
        """ Create a new event """
        data = request.get_json()
        res = EventRepository.post(data)
        if res:
            return make_response(jsonify({"status": "success"}), 201)
        else:
            return make_response(jsonify({"status": "error"}), 500)

    @staticmethod
    @swag_from('../swagger/event/PUT.yml')
    def put():
        """ Update an existing event """
        data = request.get_json()
        res = EventRepository.put(data)
        if res:
            return make_response(jsonify({"status": "success"}), 201)
        else:
            return make_response(jsonify({"status": "error"}), 500)
