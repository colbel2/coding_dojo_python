from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Show():

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    @classmethod
    def create_new_show(cls, data):
        query = "INSERT INTO shows (title, network, release_date, description, user_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s)"

        result = connectToMySQL('exam_model').query_db(query, data)

        return result

    @classmethod
    def update_show(cls,data):
        query = "UPDATE shows SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s WHERE id = %(id)s"
        connectToMySQL('exam_model').query_db(query, data)    
    
    @classmethod
    def get_all_shows(cls):
        query = "SELECT * FROM shows JOIN users ON shows.user_id=users.id;"

        results = connectToMySQL('exam_model').query_db(query)

        shows = []

        for item in results:
            new_show = cls(item)
            new_user_data = {
                'id': item['users.id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'email': item['email'],
                'password': item['password'],
                'created_at': item['users.created_at'],
                'updated_at': item['users.updated_at']
            }
            new_user = User(new_user_data)
            new_show.creator = new_user
            shows.append(new_show)
        return shows

    @classmethod
    def get_show_by_id(cls, data):

        query = "SELECT * FROM shows JOIN users ON shows.user_id = users.id WHERE shows.id = %(id)s" 
        result = connectToMySQL('exam_model').query_db(query, data)
        show = cls(result[0])
        new_user_data = {
                'id': result[0]['users.id'],
                'first_name': result[0]['first_name'],
                'last_name': result[0]['last_name'],
                'email': result[0]['email'],
                'password': result[0]['password'],
                'created_at': result[0]['users.created_at'],
                'updated_at': result[0]['users.updated_at']
            }
        new_user = User(new_user_data)
        show.creator = new_user

        return show

    @classmethod
    def delete_show(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        connectToMySQL('exam_model').query_db(query, data)

    @staticmethod
    def validate_show(data):
        is_valid = True
        if len(data['show_title']) < 3:
            is_valid = False
            flash("TV Show Title Must Be More Than 3 Characters!")
        if len(data['show_release_date'])  < 3:
            is_valid = False
            flash("TV Release Date Not Completed Correctly (YYYY-MM-DD!")
        if len(data['show_network']) < 3:
            is_valid = False
            flash("Network Name Must Be More Than 3 Characters!")
        if len(data['show_description']) < 3:
            is_valid = False
            flash("TV Show Description Must Be More Than 3 Characters!")
        return is_valid