import connexion
import six
import mysql.connector
from flask import jsonify
from flask import Flask, request
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def add_user(body):  # noqa: E501
	body = User.from_dict(connexion.request.get_json())
	sql="Insert into users(uid,firstname,lastname) values(%s,%s,%s)"
	data = (body.uid, body.first_name, body.last_name)
	db_connection = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Trinity@123", 
	database="UID"
	)
	conn = db_connection.cursor()
	conn.execute(sql, data)
	db_connection.commit()
	return 'Record Inserted' 



def find_users():
    db_connection = mysql.connector.connect(
    host="localhost",
	user="root",
	passwd="Trinity@123",
	database="UID"
	)
    conn = db_connection.cursor()
    sql_statement = "SELECT * FROM users"
    conn.execute(sql_statement)
    output = conn.fetchall()
    resp = jsonify(output)
    return resp


def validate_user(body):
    body = User.from_dict(connexion.request.get_json())
    db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Trinity@123",
    database="UID"
    )
    conn = db_connection.cursor()
    sql = "SELECT * FROM users WHERE UID=%s And FirstName=%s And LastName=%s"
    data = (body.uid, body.first_name, body.last_name)
    conn.execute(sql,data)
    row = conn.fetchone()
    if row is None:
    	return "UID not found. Please try again !"
    else: 
    	return "Validation Successful"

