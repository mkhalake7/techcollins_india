"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from repositories import TokenRepository
from flask import make_response, request


class TokenResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from('../swagger/token/POST.yml')
    def post():
        data = request.get_json()
        res = TokenRepository.post(data)
        try:
            if res[1] == 401:
                return make_response(jsonify({"status": "bad id or password"}), 401)
        except:
            pass
        if res:
            return make_response(res, 201)
        else:
            return make_response(jsonify({"status": "error"}), 500)

