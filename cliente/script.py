
import json
import requests


def main():
    entrada = int(input("¿Qué deseas hacer? \n 1) Consultar persona \n 2) Ingresar persona \n 3) Salir \n"))
    if entrada==1:
        nombre = input("Ingrese el nombre completo de la persona a buscar: \n")
        respuesta = requests.get('http://localhost:8080/demo/one?nombre=' + nombre)
        personas =respuesta.json()
        if len(personas) > 0:
            persona = personas[0]
            nombre=persona["nombre"]
            madre=persona["madre"]
            padre=persona["padre"]
            if madre == None:
                nombre_madre="indefinido"
            else:
                nombre_madre='"'+madre['nombre']+'"'
            if padre == None:
                nombre_padre="indefinido"
            else:
                nombre_padre='"'+padre['nombre']+'"'
            print('El usuario encontrado se llama "{}" su madre es {} y su padre es {}.'.format(nombre,nombre_madre,nombre_padre))
        else:
            print("La persona que buscas NO está registrada")
    if entrada==2:
        nombre=input("¿Cuál es tu nombre? \n")
        nombre_madre=input("¿Cuál es el nombre de tu madre? (dejar en blanco para omitir) \n")
        nombre_padre=input("¿Cuál es el nombre de tu padre? (dejar en blanco para omitir) \n")
        respuesta = requests.get('http://localhost:8080/demo/add?nombre=' + nombre+ '&nombre_madre='+nombre_madre+'&nombre_padre='+nombre_padre)
        print("¡El usuario y sus padres han sido insertados exitosamente!")
    else:
        print("Gracias, hasta pronto!")
        exit()


if __name__ == '__main__':
    main()
