from flask import Flask, jsonify, request
from products import products

#  app es la aplicacion del servidor

app = Flask(__name__)



# para ponerle una ruta y que responda algo. Se puede obviar el metodo GET por que funciona así por defecto
@app.route('/ping', methods=['GET'] )
def ping():
    return jsonify({"message": "Pong"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify(products)

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name ]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"messagge": "Product not found"})


@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "products": products})

# ACTUALIZAR

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]
        })
    return jsonify({
        "message": "Product Not Found"
    })

# ELIMINAR

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if len(product_name) > 0:
        products.remove(product_name[0])
        return jsonify({
                "message": "Product Deleted",
                "products": products
            })
    return jsonify({
        "message": "Product Not Found"
    })



if __name__ == '__main__':
    app.run(debug=True, port=4000)