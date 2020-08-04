#This module will run the 'saved item' portion of PriceAid
#Daniel Austin, Summer of 2020

from flask import request, jsonify, Blueprint
from Connect import Connect
from Administrator import sendResponse

conn = Connect('database.txt')
cursor = conn.cursor
savedItems = Blueprint('savedItems',__name__)

@savedItems.route('/savedItems/addNewItem',methods=['GET'])
def addNewItem(): 
    company_name = request.args['company_name']
    name = request.args['name']
    userID = request.args['userID']
    url = request.args['url']
    image_url = request.args['image_url'] 
    price = request.args['price']
    error = False

    response = {'result' : 'null'}
    #Adds a saved item
    sql = 'INSERT INTO saved_table (userID, name, url, price, company_name,image_url) VALUES (%s, %s, %s, %s, %s, %s)'
    val = (userID, name, url, price, company_name, image_url)
    try:
        cursor.execute(sql, val)
        response['result'] = 'done'
    except Exception as err:
        response['error'] = str(err)
        error = True
   
    return sendResponse(response,error)

@savedItems.route("/savedItems/removeItem", methods=["GET"])
def removeItem():
    itemCode = request.args['itemCode']
    response = {'result' : 'null'}
    error = False

    try:
        cursor.execute("DELETE FROM saved_table WHERE itemCode = '{}'".format(itemCode))
        count = cursor.rowcount      
        response['result'] = 'done'
    except Exception as err:
        response['error'] = str(err)
        error = True
    
    return sendResponse(response,error)

@savedItems.route("/savedItems/cleanCart", methods=["GET"])
def cleanCart():
    userID = request.args['userID']
    response = {'result': 'null'}
    error = False

    try:
        #Emptys all saved items
        cursor.execute("DELETE FROM saved_table WHERE userID = '{}'".format(userID))    
        response['result'] = 'done'
    except Exception as err:
        response['error'] = str(err)
        error = True

    return sendResponse(response,error)

@savedItems.route("/savedItems/displayData", methods=["GET"])
def displayData():
    userID = request.args['userID']
    response = {'result' : 'null'}
    error = False

    try:
        #Displays all data in the saved items table, used for debugging.
        cursor.execute("SELECT * FROM saved_table WHERE userID = '{}'".format(userID))
        result = cursor.fetchall()
        response['result'] = []

        for item in result:
            response['result'].append({
                'itemCode' : item[1],
                'name' : item[2],
                'url' : item[3],
                'price' : str(item[4]),
                'company_name' : item[5],
                'image_url' : item[6]
            }) 
    except Exception as err:
        response['error'] = str(err)
        error = True

    return sendResponse(response,error)