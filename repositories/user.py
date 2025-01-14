""" Defines the User repository """

from sqlalchemy import null, or_
from models import db
from models.user import User
from flask import abort
import bcrypt


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(key):
        """ Query a user by id or username or email"""
        try:
            res = User.query.filter(User.email == key).one_or_none()
            if res:
                return res
            res_id = {}
            if key.isdigit():
                res_id = User.query.get(int(key))
            return res_id
        except Exception as e:
            print(e)
            abort(400, {'message': 'invalid value'})

    @staticmethod
    def list():
        """ list all the User"""
        return User.query.all()

    @staticmethod
    def post(data):
        """ create a user"""
        try:
            password = data['password']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user = User(name=data['name'],
                        email=data['email'],
                        password=hashed_password,
                        is_admin=data.get('is_admin', False),
                        is_active=data.get('is_active', False)
                        )
            print(user)
            user.save()
            return user
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def put(data):
        """ update a user"""
        try:
            us = User.query.get(data['id'])
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
