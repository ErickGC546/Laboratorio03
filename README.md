# Laboratorio03
<p>Requisitos</p>
<p>Framework: Django 4.x./<p>
<p>Base de Datos: SQLite.</p>


Creación del entorno Virtual
1. Crea una carpeta llamada "djangoApp03"
2. Abra el cmd y pone el comando que creará un directorio llamado "myvenv" que contiene el entorno virtual:
   <ul>F:\djangoApp03> python -m venv myvenv</ul>
3. Iniciar el entorno virtual:
   <ul>F:\djangoApp03> myvenv\Scripts\activate</ul>

   
Instalación Django
5. En la consola, ejecuta
   <ul>(myvenv)F:\djangoApp03> pip install django</ul>
6. Prueba la instalación
   <ul>(myvenv)F:\djangoApp03> python -m django --version</ul>
<br>
<br>  
Proyecto en Django
7. Ingrese a la carpeta de "lab03" Descargada anteriormente y puesto dentro de la carpeta "djangoApp03"
   <ul>(myvenv)F:\djangoApp03> cd lab03</ul>
<br>
<br>
Creación de la base de datos con SQLite3
8. Crear las tablas en la base de datos, ejecute el siguiente comando:
   <ul>(myvenv)F:\djangoApp03\lab03> python manage.py migrate</ul>
9. Incluir la aplicación gestor, ejecutar el siguiente comando:
   <ul>(myvenv)F:\djangoApp03\lab03> python manage.py makemigrations gestor</ul>
10. Para gestionar las migraciones, ejecutar el siguiente comando:
   <ul>(myvenv)F:\djangoApp03\lab03> python manage.py sqlmigrate gestor 0001</ul>
11. Ejecutar de nuevo el comando “migrate” para crear esas tablas modelos en su base de datos:
   <ul>(myvenv)F:\djangoApp03\lab03> python manage.py migrate</ul>
<br>
<br>
Crear un Superusuario para el Administrador:
   <ul>(myvenv)F:\djangoApp03\lab03> python manage.py createsuperuser
     user:erick123
     pasword:123456
     gmail:erick123@gmail.com</ul>
     <br>
Ejecucion del Proyecto
12. Ejecute el siguiente comando:
   <ul>(myvenv)F:\djangoApp03\lab03> python manage.py runserver</ul>



Abre tu navegador y ve a http://127.0.0.1:8000/admin/ para acceder al administrador de Django. Inicia sesión con el superusuario que creaste

Ve a http://127.0.0.1:8000/lista/ para ver los Propietarios, Vehículos y  Control de Ingreso y Salida



