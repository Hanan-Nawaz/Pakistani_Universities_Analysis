import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hanan12335",
    database="Pak_Universities"
)

if connection.is_connected():
    print("connected to db")

my_cursor = connection.cursor()
my_cursor.execute("CREATE DATABASE IF NOT EXISTS Pak_Universities")

my_cursor.execute("CREATE TABLE IF NOT EXISTS Uni_list (Id INT Primary Key, Name Varchar(1000), Established_date date, Sector Varchar(100), City Varchar(100), Province Varchar(100) )")

connection.close()