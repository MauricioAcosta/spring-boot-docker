#!/usr/bin/env bash

python3 script.py < input > salida1
python3 script.py < input2 > salida2
md5sum -c salidaesperada.checksum
