# Laboratorio03
<p>Requisitos</p>
<p>Framework: Django 4.x./<p>
<p>Base de Datos: SQLite.</p>


Creación del entorno Virtual
1. Crea una carpeta llamada "djangoApp03"
2. Abra el cmd y pone el comando que creará un directorio llamado "myvenv" que contiene el entorno virtual:
   <li>F:\djangoApp03> python -m venv myvenv</li>
3. Iniciar el entorno virtual:
   <li>F:\djangoApp03> myvenv\Scripts\activate</li>

   
Instalación Django
5. En la consola, ejecuta
   (myvenv)F:\djangoApp03> pip install django
6. Prueba la instalación
   (myvenv)F:\djangoApp03> python -m django --version

   
Proyecto en Django
7. Ingrese a la carpeta de "lab03" Descargada anteriormente y puesto dentro de la carpeta "djangoApp03"
   (myvenv)F:\djangoApp03> cd lab03


Creación de la base de datos con SQLite3
8. Crear las tablas en la base de datos, ejecute el siguiente comando:
   (myvenv)F:\djangoApp03\lab03> python manage.py migrate
9. Incluir la aplicación gestor, ejecutar el siguiente comando:
   (myvenv)F:\djangoApp03\lab03> python manage.py makemigrations gestor
10. Para gestionar las migraciones, ejecutar el siguiente comando:
   (myvenv)F:\djangoApp03\lab03> python manage.py sqlmigrate gestor 0001
11. Ejecutar de nuevo el comando “migrate” para crear esas tablas modelos en su base de datos:
   (myvenv)F:\djangoApp03\lab03> python manage.py migrate


Crear un Superusuario para el Administrador:
   (myvenv)F:\djangoApp03\lab03> python manage.py createsuperuser
     user:erick123
     pasword:123456
     gmail:erick123@gmail.com
     
Ejecucion del Proyecto
12. Ejecute el siguiente comando:
   (myvenv)F:\djangoApp03\lab03> python manage.py runserver



Abre tu navegador y ve a http://127.0.0.1:8000/admin/ para acceder al administrador de Django. Inicia sesión con el superusuario que creaste

Ve a http://127.0.0.1:8000/lista/ para ver los Propietarios, Vehículos y  Control de Ingreso y Salida



