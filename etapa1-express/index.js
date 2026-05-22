const express = require('express');

const app = express();
const PORT = 3000;

// Middleware para leer JSON
app.use(express.json());

// PRODUCTOS
const productos = [
    { id: 1, nombre: "Procesador AMD Ryzen 5", precio: 210000 },
    { id: 2, nombre: "Memoria RAM 16GB DDR4", precio: 55000 },
    { id: 3, nombre: "Placa de Video RTX 4060", precio: 450000 },
    { id: 4, nombre: "Disco SSD NVMe 1TB", precio: 85000 },
    { id: 5, nombre: "Fuente 750W 80 Plus Gold", precio: 120000 }
];

// El carrito empieza vacío
let carrito = [];

// 1. LISTAR PRODUCTOS
app.get('/productos', (req, res) => {
    res.json(productos);
});

// 2. AGREGAR AL CARRITO
app.post('/carrito', (req, res) => {
    const { id } = req.body;

    const productoEncontrado = productos.find(p => p.id === id);

    if (productoEncontrado) {
        carrito.push(productoEncontrado);

        return res.status(201).json({
            mensaje: "Producto agregado",
            carrito
        });
    }

    res.status(404).json({
        error: "Producto no encontrado"
    });
});

// 3. VER PRODUCTOS DEL CARRITO
app.get('/carrito', (req, res) => {
    res.json(carrito);
});

// 4. VER TOTAL DEL CARRITO
app.get('/carrito/total', (req, res) => {
    const total = carrito.reduce((acc, producto) => {
        return acc + producto.precio;
    }, 0);

    res.json({
        total,
        cantidad: carrito.length
    });
});

// 5. ELIMINAR DEL CARRITO
app.delete('/carrito/:producto_id', (req, res) => {
    const productoId = parseInt(req.params.producto_id);

    const longitudInicial = carrito.length;

    carrito = carrito.filter(p => p.id !== productoId);

    if (carrito.length < longitudInicial) {
        return res.status(200).json({
            mensaje: "Producto eliminado",
            carrito
        });
    }

    res.status(404).json({
        error: "Producto no encontrado en el carrito"
    });
});

// INICIAR SERVIDOR
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});