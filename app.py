from flask import Flask, jsonify, request

app = Flask(__name__)

# PRODUCTOS
productos = [
    {"id": 1, "nombre": "Procesador AMD Ryzen 5", "precio": 210000},
    {"id": 2, "nombre": "Memoria RAM 16GB DDR4", "precio": 55000},
    {"id": 3, "nombre": "Placa de Video RTX 4060", "precio": 450000},
    {"id": 4, "nombre": "Disco SSD NVMe 1TB", "precio": 85000},
    {"id": 5, "nombre": "Fuente 750W 80 Plus Gold", "precio": 120000}
]

# El carrito empieza vacío
carrito = []

# 1. LISTAR PRODUCTOS
@app.route('/productos', methods=['GET'])
def listar_productos():
    return jsonify(productos)

# 2. AGREGAR AL CARRITO
@app.route('/carrito', methods=['POST'])
def agregar_al_carrito():
    data = request.json
    producto_id = data.get('id')
    producto_encontrado = next((p for p in productos if p['id'] == producto_id), None)

    if producto_encontrado:
        carrito.append(producto_encontrado)
        return jsonify({"mensaje": "Producto agregado", "carrito": carrito}), 201
    return jsonify({"error": "Producto no encontrado"}), 404


# PARA VISUALIZAR PRODUCTOS DEL CARRITO
@app.route('/carrito', methods=['GET'])
def ver_carrito():
    return jsonify(carrito)


# 3. VER TOTAL DEL CARRITO
@app.route('/carrito/total', methods=['GET'])
def obtener_total():
    total = sum(p['precio'] for p in carrito)
    return jsonify({"total": total, "cantidad": len(carrito)})

# 4. ELIMINAR DEL CARRITO
@app.route('/carrito/<int:producto_id>', methods=['DELETE'])
def eliminar_del_carrito(producto_id):
    global carrito
    longitud_inicial = len(carrito)
    # Filtramos: dejamos todos los que NO coinciden con el ID
    carrito = [p for p in carrito if p['id'] != producto_id]
    
    if len(carrito) < longitud_inicial:
        return jsonify({"mensaje": "Producto eliminado", "carrito": carrito}), 200
    return jsonify({"error": "Producto no encontrado en el carrito"}), 404
