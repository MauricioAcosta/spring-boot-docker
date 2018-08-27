# spring-boot-docker
Se realizara una servicios RESTful con gradle utilizando spring boot + java y base de datos postgresql, junto un cliente en python3


Los requerimientos para poder correr el proyecto son: 
- Postgresql versión 9.5
- JDK 8
- spring boot con gradle
- python3
- liberia de python requests

y si quieres utilizar los contenedores debes tener docker

Ingresa a la carpeta <a href="https://github.com/MauricioAcosta/spring-boot-docker/tree/master/RESTful">RESTful</a> y ejecuta los siguientes comandos una vez tengas los requerimientos instalados y la base de datos corriendo en el puerto de postgres por defecto (tambien debes crear una base de datos, (para este proyecto el nombre de la base de datos es <b>myDB</b>).

```
./gradlew build
java -jar build/libs/*.jar
```
o ejeuta el script
```
./ejecutar_restful.sh 
```

Luego ingresa a la carpeta <a href="https://github.com/MauricioAcosta/spring-boot-docker/tree/master/cliente">cliente</a> y ejecuta el script de python3

```
python3 script.py
# si no tienes instalados los requerimientos ejecuta
pip3 install -r requirements.txt
```
o si deseas ver la prueba automatizada puedes ejecutar el script <a href="https://github.com/MauricioAcosta/spring-boot-docker/blob/master/cliente/ejecutar_tests.sh">ejecutar_tests.sh</a>

```
./ejecutar_tests.py
```



