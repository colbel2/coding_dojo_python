from ..config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.favorite_books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        authors = []
        results = connectToMySQL('ninjas').query_db(query)
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('ninjas').query_db(query,data)

    @classmethod
    def unfavorited_dojos(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id NOT IN ( SELECT dojo_id FROM favorites WHERE ninja_id = %(id)s );"
        authors = []
        results = connectToMySQL('ninjas').query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return dojos

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (dojo_id,ninja_id) VALUES (%(dojo_id)s,%(ninja_id)s);"
        return connectToMySQL('ninjas').query_db(query,data);


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN favorites ON dojos.id = favorites.dojo_id LEFT JOIN ninjas ON ninjas.id = favorites.ninja_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('ninjas').query_db(query,data)

        # Creates instance of author object from row one
        author = cls(results[0])
        # append all book objects to the instances favorites list.
        for row in results:
            # if there are no favorites
            if row['ninjas.id'] == None:
                break
            # common column names come back with specific tables attached
            data = {
                "id": row['ninjas.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorite_books.append(ninja.Book(data))
        return author