#!/usr/bin/env bash

# Descargamos la imagen de postgres
docker pull postgres:9.5 &
docker run -rm postgres &


# contruimos el contenedor de docker y lo ejecutamos
docker build RESTful/ -t servidor &
docker run --rm -ti -p 8080:8080 -u root servidor &


# contruimos el contenedor de docker por el lado del cliete y corremos la prueba
docker build cliente/ -t cliente &
docker run -it --rm cliente &
