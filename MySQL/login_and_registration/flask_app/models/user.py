from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User():

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_user_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('login_and_registration').query_db(query, data)

        if len(result) == 0:
            return None
        else:
            return cls(result[0])

    @classmethod
    def create_new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('login_and_registration').query_db(query,data)

    @staticmethod
    def validate_new_user(data):
        is_valid = True
        if len(data['first_name']) < 2 or len(data) > 45:
            is_valid = False
            flash("Oops! Please enter your first name!")
        if len(data['last_name']) < 2 or len(data) > 45:
            is_valid = False
            flash("Oops! Please enter your last name!")    
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Please provide a valid email!")
        else:
            if User.get_user_by_email(data) != None:
                is_valid = False
                flash("Email is already registered!")
        if len(data['password']) <8:
            is_valid = False
            flash("Please use a password of at least 8 characters!")
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("The passwords do not match, please try again!")
        return is_valid