Instrucciones para correrlo como contenedor

1. Abrir docker desktop para poder usar los comandos de docker
2. Abrir la terminal y dirigirte a la carpeta del proyecto
3. Ejecutar el siguiente comando para crear la imagen:  docker build -t (nombre que elijas para la imagen) .
4. Una vez creada la imagen, correr el siguiente comando: docker run -t -i (nombre que hayas elegido para la imagen).
5. Los parametros -t y -i del comando son porque la aplicación hace uso de la consola y asi podemos acceder a la consola del contenedor.

Video https://www.youtube.com/watch?v=cBKQmuHbVvM
