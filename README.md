# Poner en marcha el proyecto  


## 1º Instalar python
https://www.python.org/
  
  
  
## 2º Clonar el repositorio
Crea una carpeta en el escritorio llamada proyecto-django por ejemplo y dentro clona el respositorio.

` git clone https://github.com/JahelCuadrado/NewsScrap.git `
  
  
  
## 3º Crear un entorno virtual
Abre una consola de comandos en la carpeta proyecto-django. Instala el paquete virtualenv.

`pip install virtualenv`

Una vez instalado crear el entorno virtual.

`virtualenv venv`

  
  
  
## 4º Activa el entorno virtual
Asegurate de que estás en la carpeta proyecto-django. Ahora activa el entorno virtual.

`.\venv\Script\activate`
  
  
  
## 5º Instala los requerimientos en el entorno virtual

`pip install ./requeriments/base.txt`



## 6º Instala los requerimientos en el entorno virtual
Descarga el archivo de secret.json pongo dentro de la carpeta newsscrap, al mismo nivel que el archivo manage.py

`https://github.com/JahelCuadrado/newsscrap-secret.json`
  
  
  
## 7º Ahora ya puedes ejecutar el servidor
Entra dentro de la carpeta 'newsscrap'

`cd newsscrap`

Y ejecuta el servidor

`python manage.py runserver`
  
  
  
## 8º Accede al servidor
Ahora el servidor ya está en marcha, puedes acceder a el a traves de:

`http://127.0.0.1:8000/`
 
