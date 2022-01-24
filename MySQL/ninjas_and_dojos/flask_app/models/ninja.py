from ..config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # list of the authors who has favorited this book
        self.authors_who_favorited = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        books = []
        results = connectToMySQL('ninjas').query_db(query)
        for row in results:
            books.append(cls(row))
        return books
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (title,num_of_pages) VALUES (%(title)s,%(num_of_pages)s);"
        return connectToMySQL('ninjas').query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM ninjas LEFT JOIN favorites ON ninjas.id = favorites.ninja_id LEFT JOIN dojos ON dojos.id = favorites.dojo_id WHERE ninjas.id = %(id)s;"
        results = connectToMySQL('ninjas').query_db(query,data)

        book = cls(results[0])

        for row in results:
            if row['books.id'] == None:
                break
            data = {
                "id": row['dojos.id'],
                "name": row['name'],
                "created_at": row['dojos.created_at'],
                "updated_at": row['dojos.updated_at']
            }
            ninja.dojos_who_favorited.append(dojo.Dojo(data))
        return ninja

    @classmethod
    def unfavorited_ninjas(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id NOT IN ( SELECT ninja_id FROM favorites WHERE dojo_id = %(id)s );"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        books = []
        for row in results:
            dojos_and_ninjas.append(cls(row))
        print( dojos_and_ninjas)
        return  dojos_and_ninjas