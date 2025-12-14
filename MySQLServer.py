import mysql.connector

def create_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF ITS NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()
create_database()

