"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import CandidateResource, GetCandidateResource

CANDIDATE_BLUEPRINT = Blueprint("candidate", __name__)

Api(CANDIDATE_BLUEPRINT).add_resource(
    CandidateResource, "/candidate/"
)
Api(CANDIDATE_BLUEPRINT).add_resource(
    GetCandidateResource, "/candidate/<string:key>"
)