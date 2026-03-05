"""
Proyecto: Generador Seguro de Contraseñas
Autor: Alejandro Fernández
Asignatura: Lógica de Programación
Descripción: Software que genera contraseñas seguras personalizadas
"""

import random
import string


def obtener_longitud():
    """
    Solicita y valida la longitud de la contraseña.
    Debe ser un número entero mayor o igual a 8.
    """
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))
            if longitud >= 8:
                return longitud
            else:
                print("Error: La longitud debe ser mayor o igual a 8.")
        except ValueError:
            print("Error: Ingrese un número válido.")


def obtener_caracteres():
    """
    Permite al usuario seleccionar los tipos de caracteres
    que incluirá la contraseña.
    """
    caracteres = ""

    if input("¿Incluir letras mayúsculas? (s/n): ").lower() == "s":
        caracteres += string.ascii_uppercase

    if input("¿Incluir letras minúsculas? (s/n): ").lower() == "s":
        caracteres += string.ascii_lowercase

    if input("¿Incluir números? (s/n): ").lower() == "s":
        caracteres += string.digits

    if input("¿Incluir símbolos? (s/n): ").lower() == "s":
        caracteres += string.punctuation

    return caracteres


def generar_contrasena(longitud, caracteres):
    """
    Genera una contraseña aleatoria usando los caracteres seleccionados.
    """
    contrasena = ""
    for _ in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena


def main():
    """Función principal del programa."""
    print("=== Generador Seguro de Contraseñas ===")

    longitud = obtener_longitud()
    caracteres = obtener_caracteres()

    if caracteres == "":
        print("Error: Debe seleccionar al menos un tipo de carácter.")
        return

    contrasena = generar_contrasena(longitud, caracteres)
    print("Contraseña generada:", contrasena)


if __name__ == "__main__":
    main()