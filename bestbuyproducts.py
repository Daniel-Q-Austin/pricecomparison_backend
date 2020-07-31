from flask import request, jsonify, Blueprint
import urllib.request, json 

bestbuyproducer = Blueprint('bestbuyproducer',__name__)

@bestbuyproducer.route('/test', methods=['GET'])
def home():
    return '''<h1>PriceAid Application</h1>
<p>API to return bestbuy pricing data based on search results.</p>'''

@bestbuyproducer.route('/products', methods=['GET'])
def api_all():
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
	return jsonify(products)