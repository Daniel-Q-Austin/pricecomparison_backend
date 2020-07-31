from flask import request, jsonify, Flask
from bestbuyproducts import bestbuyproducer

app = Flask(__name__)
app.register_blueprint(bestbuyproducer)

@app.route('/', methods=['GET'])
def main():
    return "Server is running"

@app.errorhandler(404)
def endPointNotFound(error):
    return "Endpoint not found"

if __name__ == "__main__":
    app.run()