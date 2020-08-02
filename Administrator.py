from Connect import Connect
from flask import request, jsonify, Blueprint

conn = Connect('database.txt')
administrator = Blueprint('administrator',__name__)

@administrator.route('/administration/isLoggedIn', methods=['GET'])
def isLoggedIn():
    """
    -------------------------------------------------------
    Checks login status of a user
    -------------------------------------------------------
    Parameters:
        userId - a user ID number (int)
    Returns:
        userId - a user ID number (int)
        loggedIn - the login status of the user (boolean)
    -------------------------------------------------------
    """
    loggedIn = False
    userID = request.args['userID']

    try:    
        if userID != 'null':
            sql = "SELECT loginStatus FROM administrator WHERE userID = %s"
            conn.cursor.execute(sql, (userID,))
            loggedIn = conn.cursor.fetchone()[0] == 1
    except Exception as err:
        response['error'] = err

    response = {'userID': userID, 'loggedIn': loggedIn}
    return response

@administrator.route('/administration/logIn', methods=['GET'])
def logIn():
    """
    -------------------------------------------------------
    LogIn a User
    -------------------------------------------------------
    Parameters:
        email - a user Email (String)
        password - a user Password (String)
    Returns:
        userId - a user ID number (int)
        loggedIn - the login status of the user (boolean)
    -------------------------------------------------------
    """
    email = request.args['email']
    password = request.args['password']
    userID = 'null'

    try:
        check_if_user_exist_sql = "SELECT userID FROM administrator WHERE email = %s AND password = %s"
        
        conn.cursor.execute(check_if_user_exist_sql, (email, password,))
        userID = conn.cursor.fetchone()
        
        if userID is not None:
            userID = userID[0]

        response = {'userID': userID == 'null' if userID == None else userID, 'loggedIn': False}
        if userID is not None:
            update_user_sql = "UPDATE administrator SET loginStatus = 1 WHERE userID = %s"
            conn.cursor.execute(update_user_sql, (userID,))
            response['loggedIn'] = True
    except Exception as err:
        response['error'] = err
    return response

@administrator.route('/administration/logOut', methods=['GET'])
def logOut():
    """
    -------------------------------------------------------
    LogOut a User
    -------------------------------------------------------
    Parameters:
        userId - a user ID number (int)
    Returns:
        userId - a user ID number (int)
        loggedIn - the login status of the user (boolean)
    -------------------------------------------------------
    """
    userID = request.args['userID']

    response = {'userID' : userID, 'loggedIn' : False}
    
    try:
        if userID != 'null':
            sql = "UPDATE administrator SET loginStatus = 0 WHERE userID = %s"
            conn.cursor.execute(sql, (userID,))
            response['loggedIn'] = conn.cursor.fetchall()[0] == 1    
    except Exception as err:
        response['error'] = err
    
    return response

@administrator.route('/administration/updateSettings', methods=['GET'])
def updateSettings():
    """
    -------------------------------------------------------
    Updates a user's settings
    -------------------------------------------------------
    Parameters:
        userId - a user ID number (int)
        newName - the name that the user's name should be changed to (string)
        newEmail - the email that the user's email should be changed to (string)
        newPassword - the password that the user's password should be changed to (string)   
        newPhoneNumber - the password that the user's phonenumber should be changed to (string) 
    
    Returns:
        result - a string 'done' 
    -------------------------------------------------------
    """
    userID = request.args['userID']
    newName = request.args['name'] 
    newEmail = request.args['email']
    newPassword = request.args['password'] 
    newPhoneNumber = request.args['phonenumber']

    response = {'result' : 'null'}
    try:
        sql = "UPDATE administrator SET name = %s, email = %s, password = %s, phonenumber = %s WHERE userID = %s"
        conn.cursor.execute(sql, (newName, newEmail, newPassword, userID, newPhoneNumber,))
        response['result'] = 'done'
    except Exception as err:
        response['error'] = err

    return response

@administrator.route('/administration/removeItemFromDB', methods=['GET'])
def removeItemFromDB():
    """
    -------------------------------------------------------
    Removes a user from the database if they delete their account
    -------------------------------------------------------
    Parameters:
        userId - a user ID number (int)
        
    Returns:
        result - a string 'done' 
    -------------------------------------------------------
    """
    userID = request.args['userID']

    response = {'result' : 'null'}
    try:
        sql = "DELETE FROM administrator WHERE userID = %s"
        conn.cursor.execute(sql, (userID,))
        response['result'] = 'done'
    except Exception as err:
        response['error'] = err
        
    return response

@administrator.route('/administration/addItemToDB', methods=['GET'])
def addItemToDB():
    """
    -------------------------------------------------------
    Adds a user to the database when they register their account
    -------------------------------------------------------
    Parameters:
        name - the user's name (string) 
        email - the user's email (string)
        password - the user's password (string)
    
    Returns:
        result - a string 'done' 
    -------------------------------------------------------
    """
    email = request.args['email']
    password = request.args['password']
    phonenumber = request.args['phonenumber']
    name = request.args['name']

    response = {'result' : 'null'}
    try:
        sql = "INSERT INTO administrator (loginStatus, email, password, name, phonenumber) VALUES (%d, %s, %s, %s, %s)"
        conn.cursor.execute(sql, (0 ,email, password, name, phonenumber,))
        response['result'] = 'done'
    except Exception as err:
        response['error'] = err

    return response

@administrator.route('/administration/getUserDetail', methods=['GET'])
def getUserDetail():
    """
    -------------------------------------------------------
    Get User Detail
    -------------------------------------------------------
    Parameters:
        userID - a user ID number (int)
    Returns:
        userDetail - a json object containing user details (tuple)
    -------------------------------------------------------
    """
    userID = request.args['userID']
    userDetail = 'null'

    try:
        if userID != 'null':
            sql = "SELECT * FROM administrator WHERE userID = %s"
            conn.cursor.execute(sql, (userID,))
            userDetail = conn.cursor.fetchone()
    except Exception as err:
        response['error'] = err

    response = {'userDetail': userDetail}
    return response