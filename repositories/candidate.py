""" Defines the User repository """

from sqlalchemy import null, or_
from models import db
from models.candidate import Candidate
from flask import abort


class CandidateRepository:
    """ The repository for the user model """

    @staticmethod
    def get(key):
        """ Query a user by id or username or email"""
        try:
            res = Candidate.query.filter(Candidate.email == key).one_or_none()
            if res:
                return res
            res_id = {}
            if key.isdigit():
                res_id = Candidate.query.get(int(key))
            return res_id
        except Exception as e:
            print(e)
            abort(400, {'message': 'invalid value'})

    @staticmethod
    def list():
        """ list all the User"""
        return Candidate.query.all()

    @staticmethod
    def post(data):
        """ create a user"""
        try:
            candidate = Candidate(
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                stream=data['stream'],
                skill_set=data['skill_set']
            )
            print(candidate)
            candidate.save()
            return candidate
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def put(data):
        """ update a user"""
        try:
            us = Candidate.query.get(data['id'])
            if not us:
                abort(400, {'message': 'invalid user id'})
            data.pop('id')
            for key, value in data.items():
                setattr(us, key, value)
            db.session.commit()
            return us
        except Exception as e:
            print(e)
            return False
