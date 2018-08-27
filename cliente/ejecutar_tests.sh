#!/usr/bin/env bash

port=8080
link="http://apirest:$port"
printf "Wait a moment while loading api restful."
while ! curl "$link" &> /dev/null
do
  printf "."
  sleep 2
done
printf "\n"

python3 script.py < entrada1 > salida1
python3 script.py < entrada2 > salida2
md5sum -c salidaesperada.checksum
