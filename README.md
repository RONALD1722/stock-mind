# stock-mind
pagina web de inventario 
MI explicacion del app,py

Importaciones

En esta sección se cargan todas las librerías y dependencias que la aplicación necesita para funcionar correctamente.
Incluye tanto librerías estándar de Python como externas.
Flask es el núcleo del proyecto gestiona las rutas, plantillas HTML, peticiones, sesiones y respuestas al navegadorWerkzeug se usa para procesar archivos subidos
psycopg2 permite conectarse a una base de datos PostgreSQL, lo que hace posible almacenar usuarios, registros o cualquier dato de la aplicación.openpyxl se usa para generar y dar formato a reportes en Excel.
bcrypt protege las contraseñas mediante cifrado.
smtplib y MIMEText permiten enviar correos electrónicos automáticos.
También hay utilidades para manejo de fechas, rutas del sistema operativo y memoria

Configuración de Flask
Aquí se inicializa la aplicación con Flask(name) y se define la clave secreta usada para mantener las sesiones seguras.Esa clave se utiliza para proteger la información que Flask guarda internamente, como los datos de inicio de sesión.También se podrían establecer configuraciones generales, como el modo debug, la carpeta donde se suben archivos o los parámetros del servidor

Decorador de roles (requiere_rol)
Esta función define un sistema de control de acceso dentro de la aplicación.
El decorador se coloca encima de las rutas que solo ciertos tipos de usuarios pueden acceder.
Por ejemplo, si una vista está protegida con @requiere_rol('admin'), solo los usuarios con ese rol podrán entrar.
Si alguien sin permisos intenta acceder, se le redirige a la página de inicio o al login, mostrando un mensaje de error.

Configuración de carpetas
Aquí se definen rutas internas del sistema de archivos, como la carpeta donde se guardan los archivos que los usuarios suben o donde se generan los reportes.
Se utiliza el módulo os para u.bicar correctamente las rutas Esto permite que la aplicación maneje archivos de forma organizada
5. Conexión a la base de datos

El archivo se apoya en un módulo externo llamado config.py, donde se encuentran las funciones conectar() y desconectar().Estas funciones gestionan la conexión con una base de datos PostgreSQL.
con eso podemos que , la aplicacion pueda iniciar sesión, registrar usuarios, almacenar datos o consultar información.
6. Generación de reportes en Excel
Con ayuda de openpyxl, la aplicación puede crear archivos Excel (.xlsx) a partir de información almacenada en la base de datos o subida por el usurio .Además de escribir datos, también puede aplicar formato incluir imágenes y ajustar el diseño de las celdas.Los reportes pueden luego descargarse

Envío de correos electrónicos
Este módulo permite enviar correos automáticos desde la aplicación, usando el protocolo SMTP.
Se pueden generar mensajes personalizados
El sistema usa MIMEText para dar formato al contenido y smtplib para realizar el envío.
Esto convierte a la aplicación en una herramienta más interactiva y automatizada, al mantener comunicación directa con los usuarios.
8. Manejo de usuarios y sesiones
Aquí se maneja todo lo relacionado con la autenticación: inicio de sesión, cierre de sesión y control de qué usuario está activo.
Cuando un usuario se autentica correctamente, Flask guarda sus datos (como nombre o rol) en la variable de sesión.A partir de ese momento, el sistema sabe quién está navegando y qué permisos tiene.
9. Subida y descarga de archivos
El proyecto permite subir documentos o imágenes al servidor
Gracias a Flask y secure_filename, los nombres de los archivos se procesan
el usuario puede modificar su foto y subir otra imagen

Explicacion del config..py
Módulo conectar()

Este módulo establece la conexión con la base de datos PostgreSQL usando la librería psycopg2. Define los parámetros de conexión y, si todo funciona correctamente, devuelve el objeto de conexión y muestra un mensaje de éxito. En caso de error, lo detecta y muestra un mensaje sin detener el programa.

Módulo desconectar(conexion)

Este módulo cierra una conexión activa con la base de datos. Verifica que la conexión exista antes de cerrarla y muestra un mensaje al finalizar. Su función es liberar recursos y asegurar que las conexiones no queden abiertas innecesariamente.

Ejecución del servidor

Al final del archivo se encuentra la instrucción que pone en marcha la aplicación Flask.
para que, al ejecutar python app.py, el servidor se inicia y la aplicación queda disponible desde un navegador web

1. Carpeta templates/
 Función:
Es el corazón de la parte visual de tu aplicación Flask.
Contiene todas las plantillas HTML que el servidor Flask renderiza para mostrar al usuario final.
 Cómo funciona:
Flask usa la función render_template() para buscar archivos dentro de esta carpeta.
Por ejemplo:
return render_template("login.html")
mostrará el archivo templates/login.html en el navegador.

Carpeta static/
 Función:
Guarda todos los archivos estáticos Flask los sirve directamente al navegador cuando se incluyen en las páginas HTML.
Función principal:
Dar estilo y funcionalidad visual al sitio web.
Servir contenido estático directamente al navegador sin pasar por el servidor Flask

Carpeta uploads/
Esta carpeta guarda los archivos subidos por los usuarios a través de la aplicación.
Puede tratarse de imágenes, documentos, reportes, comprobantes u otros tipos de archivos permitidos.
Servir como almacenamientoque los usuarios cargan desde formularios web.

Carpeta .vscode/
Contiene configuraciones  del editor que ayudan a mantener coherencia en el formato y ejecución del proyecto.


EL convertir_claves.py sirve
sirve para incritar la contrasena Esta función recibe:
nombre: nombre completo del usuario.
usuario: nombre de usuario (login).
clave: contraseña 
rol: el tipo de usuario ( "administrador").
si alguien roba la base de datos, no podrá ver las contraseñas reales, solo los “hashes” encriptados.
