from flask import request, jsonify, Blueprint
from Connect import Connect

conn = Connect('database.txt')
customers = Blueprint('customers',__name__)

@customers.route('/customers/history', methods=['GET'])
def history():
    """
    -------------------------------------------------------
    Checks history status of a user
    Use: history = Customer.history(conn, itemCode, userID)
    -------------------------------------------------------
    Parameters:
        userId - a user ID number (int)
    Returns:
        history - the search history of the user (tuple)
    -------------------------------------------------------
    """
    itemCode=request.args['itemCode']
    userID=request.args['userID']
    response = {'history' : 'null'}
    
    try:
        if userID !='null':
            sql = "SELECT * FROM history WHERE userID = %s ORDER BY searchedDate DESC"
            conn.cursor.execute(sql, (userID,))
            response['history'] = conn.cursor.fetchall()
    except Exception as err:
        request['error'] = err
    
    return response

@customers.route('/customers/addHistory', methods=['GET'])
def addHistory():
    """
    -------------------------------------------------------
    add to user history
    -------------------------------------------------------
    Parameters:
        itemName - item's name (int)
        userId - a user ID number (int)
        searchDate - search date (datetime)
    Returns:
        updatedHistory - user's new history (boolean)
    -------------------------------------------------------
    """
    userID = request.args['userID'] 
    searchDate = request.args['searchDate']
    itemName = request.args['itemName']

    response = {'update' : False}
    if userID is not None and itemCode is not None:
        sql = "INSERT INTO history (userID, searchedDate, itemName) VALUES (%s, %s, %s)"
        conn.cursor.execute(sql, (userID, searchDate, itemName, ))
        response['update'] = True
    return response

