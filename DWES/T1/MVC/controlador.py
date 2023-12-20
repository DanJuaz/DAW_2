from wsgiref.simple_server import make_server
import vistas
import modelos

sesion = modelos.abrir_sesion()
consulta = {"id": 2}
productos = modelos.Producto.read(sesion, **consulta)
# print(productos)
modelos.cerrar_sesion(sesion)
sesion = None
# Definir la función app que manejará las solicitudes.
def app(environ, start_response):
    path = environ.get('PATH_INFO')
    # print('path: ', path)
    if path == '/':
        return vistas.english_handle_index(environ, start_response)
    elif path == '/es':
        return vistas.spanish_handle_index(environ, start_response, productos)
    elif   path.startswith('/static/'):
        return vistas.serve_static(environ, start_response)
    else:
        return vistas.handle_404(environ, start_response)


if __name__ == "__main__":
    host = 'localhost'
    port = 8000

    httpd = make_server(host, port, app)
    print(f"Servidor en http://{host}:{port}")
    httpd.serve_forever()
'''
Una vez ejecutado el controlador, podemos acceder a través del navegador, 
con las rutas: http://localhost:8000/    (no se usa jinja2)
y   http://localhost:8000/es, esta segunda usa jinja2.
Con la url http://localhost:8000/static/ se mostrará el archivo css.
Si se pone una url diferente, saldrá el mensaje de 'página no encontrada'
'''