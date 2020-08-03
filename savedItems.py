#This module will run the 'saved item' portion of PriceAid
#Daniel Austin, Summer of 2020

from flask import request, jsonify, Blueprint
from Connect import Connect
from Administrator import sendResponse

conn = Connect('database.txt')
cursor = conn.cursor
savedItems = Blueprint('savedItems',__name__)

@savedItems.route('/savedItems/addNewItem',methods=['POST'])
def addNewItem(): 
    email = request.args['email']
    company_name = request.args['company_name']
    name = request.args['name']
    userID = request.args['userID']
    url = request.args['url']
    price = request.args['price']
    error = False

    response = {'result' : 'null'}
    #Adds a saved item
    sql = 'INSERT INTO saved_table (userID, name, url, email, price, company_name) VALUES (%d, %s, %s, %s, %.2f, %s)'
    val = (userID, name, url, email, price, company_name)
    try:
        cursor.execute(sql, val)
        response['result'] = 'done'
    except Exception as err:
        response['error'] = err
        error = True

    connection.commit()
    return sendResponse(response,error)

@savedItems.route("/savedItems/removeItem", methods=["DELETE"])
def removeItem():
    itemCode = request.args['itemCode']
    response = {'result' : 'null'}
    error = False

    try:
        cursor.execute("DELETE FROM saved_table WHERE itemCode = '{}'".format(itemCode))
        count = cursor.rowcount
        connection.commit()
        response['result'] = 'done'
    except Exception as err:
        response['error'] = err
        error = True
    
    return sendResponse(response,error)

@savedItems.route("/savedItems/cleanCart", methods=["DELETE"])
def cleanCart():
    userID = request.args['userID']
    response = {'result': 'null'}
    error = False

    try:
        #Emptys all saved items
        cursor.execute("DELETE FROM saved_table WHERE userID = '%s'".format(userID))
        connection.commit()
        response['result'] = 'done'
    except Exception as err:
        response['error'] = err
        error = True

    return sendResponse(response,error)

@savedItems.route("/savedItems/displayData", methods=["GET"])
def displayData():
    userID = request.args['userID']
    response = {'result' : 'null'}
    error = False

    try:
        #Displays all data in the saved items table, used for debugging.
        cursor.execute("SELECT * FROM saved_table WHERE userID = '%s'".format(userID))
        response['result'] = cursor
    except Exception as err:
        response['error'] = err
        error = True

    return sendResponse(response,error)