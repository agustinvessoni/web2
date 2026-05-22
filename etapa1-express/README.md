# Desarrollo Web 2 - Entrega etapa 1

## Requisitos
- Node.js instalado
- npm instalado

## Instalación

1. Clonar el repositorio
2. Instalar dependencias:

```bash
npm install
```

3. Ejecutar el servidor:

```bash
node server.js
```

## Dependencias utilizadas

- Express JS


## Endpoints

### GET /productos
Lista el catálogo de hardware.

### POST /carrito
Agrega un producto al carrito.

Body JSON:
```json
{
  "id": 1
}
```

### GET /carrito
Muestra el contenido actual del carrito.

### GET /carrito/total
Muestra la suma total de precios y cantidad de productos.

### DELETE /carrito/:id
Elimina un producto del carrito según su ID.

Ejemplo:
```bash
DELETE /carrito/1
```

## Puerto utilizado
El servidor se ejecuta en:

```txt
http://localhost:3000
```