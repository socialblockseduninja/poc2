""" Defines the User repository """
import json
from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(last_name, first_name):
        """ Query a user by last and first name """
        out=  '{"age": 25, "first_name": "John", "last_name": "Doe"}'
        return json.dumps({"age": 25, "first_name": "John", "last_name": "Doe"});


    def update(self, last_name, first_name, age):
        """ Update a user's age """
        user = self.get(last_name, first_name)
        user.age = age
        out= json.dumps({'status': 'OK', 'topicDesc':'test'})
        return out;

    @staticmethod
    def create(last_name, first_name, age):
        """ Create a new user """
         
        out= json.dumps({'status': 'OK', 'topicDesc':'test'})
        return out;
