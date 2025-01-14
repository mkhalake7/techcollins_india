"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from repositories import CandidateRepository
from flask import make_response, request


def serialize(obj):
    return {
        'id': obj.id,
        'name': obj.name,
        'email': obj.email,
        'phone': obj.phone,
        'stream': obj.stream,
        'skill_set': obj.skill_set,
    }


class GetCandidateResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/candidate/GET.yml")
    def get(key):
        """ Return an user key information based on his id"""
        user = CandidateRepository.get(key=key)
        if user:
            return make_response(jsonify({"user": serialize(user)}), 200)
        else:
            return make_response(jsonify({"error": "invalid user"}), 400)


class CandidateResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/candidate/LIST.yml")
    def get():
        """ Return all the user information """
        candidates = CandidateRepository.list()
        return make_response(jsonify({"list_candidates": [serialize(candidate) for candidate in candidates]}), 200)

    @staticmethod
    @swag_from('../swagger/candidate/POST.yml')
    def post():
        data = request.get_json()
        res = CandidateRepository.post(data)
        if res:
            return make_response(jsonify({"status": "success"}), 201)
        else:
            return make_response(jsonify({"status": "error"}), 500)

    # @staticmethod
    # @swag_from('../swagger/user/PUT.yml')
    # def put():
    #     data  =  request.get_json()
    #     res = UserRepository.put(data)
    #     if res:
    #         return make_response(jsonify({"status":"success"}),201)
    #     else:
    #         return make_response(jsonify({"status":"error"}),500)
