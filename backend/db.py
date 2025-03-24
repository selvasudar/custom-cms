import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="my_cms",
        port=8889,  # MAMP's MySQL port
        unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock"  # MAMP socket path
    )
