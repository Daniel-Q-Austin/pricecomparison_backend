"""
This artificat is implemented as an API using flask.
It retrieves the first ten product results from BestBuy's website based on a user input keyword. ItemName, price, url, retailer name, imageUrl are retrieved.
Returns the list of products in json format.
Programmer: Daniel Zhou
Variables:
    search: Keyword to search (string)
    data: Retrieves name, price, and url of items/products (dictionary)
    products: List of retrieved products. Returned in json format.
"""
from flask import request, jsonify, Blueprint
import urllib.request, json 
from Administrator import sendResponse

bestbuyproducts = Blueprint('bestbuyproducts',__name__)

@bestbuyproducts.route('/bestbuyproducts/products', methods=['GET'])
def api_all():
	error = False

	response = {'result': 'null'}
	try:
		if 'search' in request.args:
			search = request.args['search']
		else:
			response['error_2'] = "Error: No search field provided. Please search for products."
        link = "https://api.bestbuy.com/v1/products(search={})?format=json&show=name,salePrice,addToCartUrl,largeImage&apiKey=N0ReEPP28MPw3Gd2xSIAQ5dM".format(search)
        data = json.loads(urllib.request.urlopen(link).read().decode())
        products = data['products']
        for item in products:
            item['url']  = item.pop('addToCartUrl')
            item['retailer'] = 'BestBuy'
        products = sorted(products, key = lambda i: i['salePrice']) 
		response['result'] = products
	except Exception as err:
		response['error'] = str(err)
		error = True
	
	return sendResponse(response, error)