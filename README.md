Desarrollo Web 2 - Entrega etapa 1

## Instalación
1. Crear entorno virtual: `python -m venv env`
2. Activar entorno: `env\Scripts\activate` (Windows)
3. Instalar Flask: `pip install flask`
4. Ejecutar el servidor: `flask run`

## Endpoints
- **GET /productos**: Lista el catálogo de hardware.
- **POST /carrito**: Agrega un producto (enviar `{"id": X}`).
- **GET /carrito**: Muestra el contenido actual del carrito.
- **GET /carrito/total**: Muestra la suma de precios.
- **DELETE /carrito/<id>**: Elimina un producto por su ID.