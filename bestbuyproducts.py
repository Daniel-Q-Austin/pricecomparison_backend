from flask import request, jsonify, Blueprint
import urllib.request, json 

bestbuyproducts = Blueprint('bestbuyproducts',__name__)

@bestbuyproducts.route('/bestbuyproducts/products', methods=['GET'])
def api_all():
	
	response = {'result': 'null'}
	try:
		if 'search' in request.args:
			search = request.args['search']
		else:
			return "Error: No search field provided. Please search for products."
		link = "https://api.bestbuy.com/v1/products(search={})?format=json&show=sku,name,salePrice&apiKey=N0ReEPP28MPw3Gd2xSIAQ5dM".format(search)
		data = json.loads(urllib.request.urlopen(link).read().decode())
		products = data['products']
		for item in products:
			del item["sku"]
		products = sorted(products, key = lambda i: i['salePrice']) 
		response['result'] = jsonify(products)
	except Exception as err:
		response['error'] = err
	
	return response