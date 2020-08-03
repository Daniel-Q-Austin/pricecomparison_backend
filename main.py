from flask import request, jsonify, Flask, Response
from bestbuyproducts import bestbuyproducts
from savedItems import savedItems
from Administrator import administrator, sendResponse
from customers import customers
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(bestbuyproducts)
app.register_blueprint(savedItems)
app.register_blueprint(administrator)
app.register_blueprint(customers)

@app.route('/', methods=['GET'])
def main():
    return sendResponse("Server is running", False)

@app.errorhandler(404)
def endPointNotFound(error):
    return sendResponse("Endpoint not found", True)

if __name__ == "__main__":
    app.run()