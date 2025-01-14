""" Defines the User repository """
from models.user import User
from flask import abort
import bcrypt
from flask import jsonify
from flask import request
from flask_jwt_extended import create_access_token


class TokenRepository:
    """ The repository for the user model """

    @staticmethod
    def post(data):
        """ create a user"""
        try:
            email = data['email']
            password = data['password']
            user_data = User.query.filter(User.email == email).one_or_none()

            if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data.password):
                access_token = create_access_token(identity=email)
                return jsonify(access_token=access_token)
            else:
                return jsonify({"msg": "Bad username or password"}), 401

        except Exception as e:
            return False
