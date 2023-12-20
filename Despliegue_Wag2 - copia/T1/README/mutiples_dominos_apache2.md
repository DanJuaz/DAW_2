# Mutiples dominios en apache
## Modificar arhivo de hosts
Incluir todas las rutas que se necesiten
```python
sudo nano /etc/hosts
```
```
127.0.0.1 dominio1.com
127.0.0.1 dominio2.com
127.0.0.1 dominio3.com
```
```
Ctr + x -> Leave nano
```
## Crear rutas y repositorios para los dominios
```
sudo mkdir /var/www/html domini1.com
...
```
## Configuracion por defecto y de los dominios
Em:
```
/etc/apache2/sites-available
	000-default.conf  default-ssl.conf
```
## Cada dominio tendrá su propia configuración
```
sudo cp 000-default.conf dominio1.conf
sudo cp 000-default.conf dominio2.conf
sudo cp 000-default.conf dominio3.conf
```
## Configuracion del dominio
```sudo nano dominio1.conf```
```
<VirtualHost *:80>
        #error 404 ponganse en contacto con:
        ServerAdmin admin@dominio1.com
        #nombre del servidor
        ServerName dominio1.com
        #redirigir a dominio1.com
        DocumentRoot /var/www/html/dominio1.com
	
        #errores, crear para cada dominio un archivo error.log
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
```
## Activar los archivos de configuración de cada dominio
```
cd /etc/apache2/sites-available
sudo a2ensite dominio1.conf
sudo a2ensite dominio2.conf
sudo a2ensite dominio3.conf
```
## Testear si tiene algún error los archivos de configuración
```
sudo apache2ctl configtest
```
## Renovar el contenido y  la configuración del dominio 
```
sudo systemctl reload apache2
```
## Visualizar
```
curl dominio1.com
curl dominio2.com
curl dominio3.com
```
```
http://192.168.1.63/dominio1.com/
http://192.168.1.63/dominio2.com/
http://192.168.1.63/dominio3.com/
```
## Ver Ip
```
ip a | grep inet
ip a

```