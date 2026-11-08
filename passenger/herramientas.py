import os

def limpiar_pantalla():
    os.system("clear" if os.name == "posix" else "cls")

def pausar():
    input("\nPresione Enter para continuar...")

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")

def pedir_cedula_valida():
    while True:
        try:
            cedula = input("Ingrese su cédula (10 dígitos): ").strip()
            
            # Validación de 10 dígitos numéricos
            if not (cedula.isdigit() and len(cedula) == 10):
                raise ValueError("Cédula inválida. Debe contener exactamente 10 dígitos numéricos.")
            return cedula

        except ValueError as e:
            print(f"Error: {e} Intente nuevamente.\n")

from datetime import datetime

def pedir_fecha_valida():
    while True:
        try:
            fecha_str = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
            
            # Intenta parsear la cadena con el formato exacto AAAA-MM-DD
            datetime.strptime(fecha_str, "%Y-%m-%d")
            
            return fecha_str  # Si no falla, la fecha es válida calendáricamente

        except ValueError:
            print("  Error: Fecha inválida. Debe usar el formato AAAA-MM-DD y ser una fecha real. Intente nuevamente.\n")

def menu(titulo, opciones):
    print(f"\n===== {titulo} =====")
    for opcion in opciones:
        print(f"{opcion}")
    lon = len(opciones)-1
    return leer_entero(f"Elige una opción (0-{lon}): ")
