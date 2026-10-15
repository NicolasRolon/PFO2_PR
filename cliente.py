import requests

URL = "http://127.0.0.1:5000"
sesion = requests.Session()


def registrar():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    respuesta = sesion.post(
        URL + "/registro",
        json={"usuario": usuario, "contraseña": contraseña}
    )

    print(respuesta.json())


def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    respuesta = sesion.post(
        URL + "/login",
        json={"usuario": usuario, "contraseña": contraseña}
    )

    print(respuesta.json())


def ver_tareas():
    respuesta = sesion.get(URL + "/tareas")
    print(respuesta.text)


while True:
    print("\n1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Ver tareas")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        registrar()
    elif opcion == "2":
        login()
    elif opcion == "3":
        ver_tareas()
    elif opcion == "4":
        break
    else:
        print("Opción incorrecta")
