"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from repositories import UserRepository
from flask import make_response, request

def serialize(obj):
    return {
            'id': obj.id,
            'name': obj.name,
            'email': obj.email,
            'is_admin': obj.is_admin,
            'is_active': obj.is_active,
           }

class GetUserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/user/GET.yml")
    def get(key):
        """ Return an user key information based on his id"""
        user = UserRepository.get(key=key)
        if user:
            return make_response(jsonify({"user": serialize(user)}),200)
        else:
            return make_response(jsonify({"error": "invalid user"}),400)

class UserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/user/LIST.yml")
    def get():
        """ Return all the user information """
        users = UserRepository.list()
        return make_response(jsonify({"list_user": [serialize(user) for user in users]}),200)
    
    @staticmethod
    @swag_from('../swagger/user/POST.yml')
    def post():
        data = request.get_json()
        res = UserRepository.post(data)
        if res:
            return make_response(jsonify({"status":"success"}),201)
        else:
            return make_response(jsonify({"status":"error"}),500)

    @staticmethod
    @swag_from('../swagger/user/PUT.yml')
    def put():
        data  =  request.get_json()
        res = UserRepository.put(data)
        if res:
            return make_response(jsonify({"status":"success"}),201)
        else:
            return make_response(jsonify({"status":"error"}),500)



