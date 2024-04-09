# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de tu aplicación al contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 para que la aplicación Flask pueda ser accedida desde fuera del contenedor
EXPOSE 5000

# Ejecuta la aplicación Flask cuando se inicie el contenedor
CMD ["python", "app.py"]
