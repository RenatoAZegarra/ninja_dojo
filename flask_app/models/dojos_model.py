from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninjas_model

class Dojo:
    def __init__( self, data ):
        self.id = data['id']
        self.name_of_dojo = data['name_of_dojo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( name_od_dojos , created_at , updated_at ) VALUES (%(name_of_dojo)s,NOW(),NOW());"
        result= connectToMySQL(DATABASE).query_db( query, data)
        return result
    @classmethod
    def get_all( cls ):
        query  = "SELECT * "
        query += "FROM dojos;"

        result = connectToMySQL( DATABASE ).query_db( query )

        list_of_dojos = []
        for row in result:
            list_of_dojos.append( cls( row ) )
        return list_of_dojos

    @classmethod
    def create_one( cls, data ):
        query  = "INSERT INTO dojos( name_of_dojo, created_at, updated_at ) "
        query += "VALUES ( %(name_of_dojo)s, NOW(), NOW() )"

        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result
    
    @classmethod
    def get_one_dojo( cls, data ):
        query  = "SELECT * "
        query += "FROM dojos d LEFT JOIN ninjas n "
        query += "ON n.dojo_id = d.id "
        query += "WHERE d.id = %(dojo_id)s;"

        results = connectToMySQL( DATABASE ).query_db( query, data )
        dojo = cls ( results[0])

        for row in results:

                ninja_data= {
                    "id" : row["n.id"],
                    "first_name" : row["first_name"],
                    "last_name" : row["last_name"],
                    "age" : row["age"],
                    "created_at" : row["n.created_at"],
                    "updated_at" : row["n.updated_at"]
                }
                dojo.ninjas.append( ninjas_model.Ninja( ninja_data))
        return dojo
