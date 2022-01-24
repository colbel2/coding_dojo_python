from ..config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas = []
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        for row in results:
            ninjas.append(cls(row))
        return ninjas
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name,last_name, age) VALUES (%(first_name)s,%(last_name)s,%(age)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM ninjas LEFT JOIN show ON ninjas.id = show.ninja_id LEFT JOIN dojos ON dojos.id = show.dojo_id WHERE ninjas.id = %(id)s;"
        results = connectToMySQL('ninjas').query_db(query,data)

        ninja = cls(results[0])

        for row in results:
            if row['dojos.id'] == None:
                break
            data = {
                "id": row['dojos.id'],
                "name": row['name'],
                "created_at": row['dojos.created_at'],
                "updated_at": row['dojos.updated_at']
            }
            
        return ninja

