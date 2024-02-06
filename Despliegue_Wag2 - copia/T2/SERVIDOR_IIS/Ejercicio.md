**Práctica 1: Configuración Básica del Sitio Web en IIS**

1. **Creación de la estructura de carpetas y archivos:**
   - Instalción de servidor IIS(Adminstrar->Agregar Roles y caracteristicas):
   - ![Alt text](image.png)
   - ![Alt text](image-1.png)
   - ![Alt text](image-2.png)
   - Crea una página sencilla llamada `index.html`.
   - Crea una carpeta llamada `Miweb` dentro de `C:\inetpub\wwwroot`.
    - ![Alt text](image-3.png)

2. **Añadir el sitio web en IIS:**

   - Abre la consola de Administrador de Internet Information Services (IIS).
   - ![Alt text](image-4.png)
   - En el árbol de la izquierda, haz clic derecho en `Sitios` y selecciona `Agregar sitio web`.
   - ![Alt text](image-5.png)
   - Completa los campos requeridos, como el nombre del sitio web y la ruta física (en este caso, `C:\inetpub\wwwroot\Miweb`).
   - Asigna un puerto (generalmente el 80 para HTTP) y, opcionalmente, una dirección IP.
   - Haz clic en `Aceptar` para crear el sitio web.
   ![Alt text](image-6.png)

3. **Configuración del documento predeterminado:**
   - En la consola de IIS, selecciona tu sitio web.
   - En la sección de `Documentos predeterminados`, añade `index.html` como documento predeterminado si no está presente.
   - ![Alt text](image-7.png)
   - ![Alt text](image-8.png)

4. **Creación de un nombre DNS para el sitio web:**
   - Abre la consola de administración de DNS en el servidor.
   - ![Alt text](image-9.png)
   - Agrega una entrada de tipo `A` o `CNAME` para asignar un nombre DNS a la dirección IP del servidor donde está alojado el sitio web.
   - ![Alt text](image-10.png)
   - ![Alt text](image-11.png)

5. **Actualizar el servidor web y el sitio:**
   - Guarda todos los cambios realizados.
   - ![Alt text](image-12.png)

**Práctica 5: Habilitar Autenticación Básica en IIS**

1. **Agregar el rol de Autenticación Básica:**
   - Abre la consola de Administrador de Internet Information Services (IIS).
   - Navega hasta `Servidor web IIS -> Seguridad -> Autenticación básica`.
   - Habilita la autenticación básica.
   - ![Alt text](image-14.png)

2. **Reiniciar el servidor web:**
   - Desde el símbolo del sistema, ejecuta el comando `iisreset` para reiniciar el servidor web y aplicar los cambios.
   - ![Alt text](image-12.png)
   - ![Alt text](image-15.png)

3. **Configurar la autenticación para el sitio web:**
   - En la consola de IIS, selecciona tu sitio web.
   - En la sección de `Autenticación`, deshabilita la autenticación anónima y habilita la autenticación básica.
   - ![Alt text](image-13.png)

4. **Reiniciar el servicio de IIS si es necesario:**
   - Detén y vuelve a iniciar el servicio de IIS desde la consola de servicios si los cambios no se aplican correctamente.
   - ![Alt text](image-12.png)

5. **Comprobar la autenticación:**
   - Accede al sitio web desde un navegador.
   - Debería solicitarte un usuario y una contraseña para la autenticación básica.