# Documentación aplicación Flask:
Se ha creado un repositorio en GitHub desde el que cada integrante del equipo puede acceder para obtener los archivos que conforman la aplicación.
    Acceso: https://github.com/chemapm/lab100.git
    git clone https://github.com/chemapm/lab100.git
Se trabajará en 2 entornos, uno de producción sobre el cual está el trabajo real en ejecución al que acceden los usuarios y uno de desarrollo el cual será una copia del entorno de producción, y será la base sobre el que los integrantes trabajarán. Por último cada integrante desarrollará su trabajo en local, y una vez testeado y aprobado se actualizará en el entorno de desarrollo para que el resto del equipo tenga acceso. 
Una vez clonado el repositorio GitHub instalar dependencias:
    pip install -r requirements.txt
Para poder actualizar la aplicación primero ha de probarse que pasa los test en local y que cubre al menos el 80% de las líneas de código. En estos test se comprueba que se puede añadir, eliminar y ver los datos, además del funcionamiento del modelo.
Estos test se ejecutan con los siguientes comandos:
    coverage run -m pytest
    coverage report -m
Para iniciar aplicación ejecutar los siguientes comandos:
    export Flask_env = local		# Selección de configuración de entorno
    python manage.py		# genera tabla en base de datos
	python run.py 			# inicia aplicación

# Documentación aplicación Jenkins:
Instalar Jenkins a partir de imagen Docker: https://www.jenkins.io/doc/book/installing/docker/
Para tener un job que se ejecute ante cada cambio en el repositorio se ha creado a partir de un pipeline de SCM en el que se ha añadido el enlace al repositorio GitHub además de las credenciales necesarias para permitir el acceso. También se han añadido las credenciales de Docker Hub para poder cargar la imagen. Jenkins se encarga mediante una opción del job (webhook) de ejecutarse autamáticamente si ha habido cambios en el repositorio Git en alguna de las ramas main o develop. Esto se ha conseguido realizar pese a utilizar Jenkins como localhost gracias a ngrok.
