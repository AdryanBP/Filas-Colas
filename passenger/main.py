from herramientas import (
    leer_entero,
    limpiar_pantalla,
    menu,
    pausar,
    pedir_cedula_valida,
    pedir_fecha_valida,
)
from mi_cola import MiCola
from mi_pila import MiPila
from pasajero import Pasajero


def leer_pasajero():
    print("\n--- Registro de Datos del Pasajero ---")
    numero = leer_entero("  N.º Identificador: ")
    nombre = input("  Nombre completo: ").strip()
    cedula = pedir_cedula_valida()
    edad = leer_entero("  Edad: ")
    fecha = pedir_fecha_valida()
    destino = input("  Ciudad destino: ").strip()
    asiento = input("  Código de asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Retorna 5 pasajeros de prueba en orden de llegada."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


# ---------------------- OPERACIONES AUXILIARES ----------------------
def operacion_buscar(estructura):
    num = leer_entero("  Ingrese el N.º de pasajero a consultar: ")
    pos = estructura.buscar(num)
    if pos != -1:
        print(f"\n[+] Coincidencia en índice [{pos}]:")
        print(f"    {estructura.datos[pos]}")
    else:
        print(f"\n[-] Registro no encontrado: No existe el pasajero N.º {num}.")


def operacion_modificar(estructura):
    num = leer_entero("  Ingrese el N.º de pasajero a actualizar: ")
    nuevo_destino = input("  Nuevo destino: ").strip()
    nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
    if estructura.modificar(num, nuevo_destino, nuevo_asiento):
        print(f"\n[+] Pasajero #{num} actualizado correctamente.")
    else:
        print(f"\n[-] No se pudo modificar: Pasajero #{num} inexistente.")


def operacion_eliminar(estructura):
    num = leer_entero("  Ingrese el N.º de pasajero a remover: ")
    if estructura.eliminar_por_numero(num):
        print(f"\n[+] Pasajero #{num} retirado de la estructura.")
    else:
        print(f"\n[-] Error al remover: Pasajero #{num} no encontrado.")


# ---------------------- MENÚ PILA ----------------------
def menu_pila(pila):
    opciones = [
        "0. Regresar al menú principal",
        "1. Apilar nuevo pasajero",
        "2. Desapilar pasajero",
        "3. Consultar tope",
        "4. Visualizar contenido completo",
        "5. Consultar estado y tamaño actual",
        "6. Localizar pasajero por número",
        "7. Actualizar destino y asiento",
        "8. Remover pasajero específico",
        "9. Clonar pila actual",
        "10. Cargar registros de prueba",
    ]

    while True:
        limpiar_pantalla()
        op = menu("GESTIÓN DE PASAJEROS · ESTRUCTURA PILA (LIFO)", opciones)

        if op == 0:
            break

        limpiar_pantalla()
        if op == 1:
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print(f"\n[+] Elemento insertado en el tope: {pasajero.nombre} (#{pasajero.numero})")
            else:
                print("\n[!] Desbordamiento: La pila alcanzó su capacidad máxima.")

        elif op == 2:
            removido = pila.desapilar()
            if removido:
                print(f"\n[-] Elemento desapilado: {removido}")
            else:
                print("\n[!] Subdesbordamiento: La pila se encuentra vacía.")

        elif op == 3:
            tope = pila.ver_tope()
            if tope:
                print(f"\n[i] Elemento en el tope actual:\n    {tope}")
            else:
                print("\n[i] La pila no contiene elementos.")

        elif op == 4:
            print("[i] Listado de pasajeros (Tope -> Base):")
            pila.listar()

        elif op == 5:
            estado = "Vacía" if pila.esta_vacia() else "Con elementos"
            print(f"\n[i] Métricas de la pila:")
            print(f"    - Cantidad de elementos : {pila.longitud()}")
            print(f"    - Estado actual         : {estado}")

        elif op == 6:
            operacion_buscar(pila)

        elif op == 7:
            operacion_modificar(pila)

        elif op == 8:
            operacion_eliminar(pila)

        elif op == 9:
            copia = pila.copiar()
            print("[+] Pila clonada exitosamente. Registros en la nueva instancia:")
            copia.listar()

        elif op == 10:
            for p in datos_prueba():
                pila.apilar(p)
            print("[+] Lote de 5 pasajeros de prueba cargado a la pila.")

        else:
            print("[!] Opción inválida. Intente nuevamente.")

        pausar()


# ---------------------- MENÚ COLA ----------------------
def menu_cola(cola):
    opciones = [
        "0. Regresar al menú principal",
        "1. Encolar nuevo pasajero",
        "2. Desencolar pasajero",
        "3. Consultar frente",
        "4. Visualizar cola completa",
        "5. Consultar estado y tamaño actual",
        "6. Localizar pasajero por número",
        "7. Actualizar destino y asiento",
        "8. Remover pasajero específico",
        "9. Clonar cola actual",
        "10. Cargar registros de prueba",
    ]

    while True:
        limpiar_pantalla()
        op = menu("GESTIÓN DE PASAJEROS · ESTRUCTURA COLA (FIFO)", opciones)

        if op == 0:
            break

        limpiar_pantalla()
        if op == 1:
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print(f"\n[+] Pasajero posicionado al final de la cola: {pasajero.nombre} (#{pasajero.numero})")
            else:
                print("\n[!] Desbordamiento: La cola alcanzó su capacidad máxima.")

        elif op == 2:
            removido = cola.desencolar()
            if removido:
                print(f"\n[-] Pasajero atendido y retirado: {removido}")
            else:
                print("\n[!] Subdesbordamiento: La cola se encuentra vacía.")

        elif op == 3:
            frente = cola.ver_frente()
            if frente:
                print(f"\n[i] Primer pasajero por atender (Frente):\n    {frente}")
            else:
                print("\n[i] No hay elementos en la cola.")

        elif op == 4:
            print("[i] Listado de la cola (Frente -> Final):")
            cola.listar()

        elif op == 5:
            estado = "Vacía" if cola.esta_vacia() else "Con elementos"
            print(f"\n[i] Métricas de la cola:")
            print(f"    - Pasajeros en espera   : {cola.longitud()}")
            print(f"    - Estado actual         : {estado}")

        elif op == 6:
            operacion_buscar(cola)

        elif op == 7:
            operacion_modificar(cola)

        elif op == 8:
            operacion_eliminar(cola)

        elif op == 9:
            copia = cola.copiar()
            print("[+] Cola clonada exitosamente. Registros en la nueva instancia:")
            copia.listar()

        elif op == 10:
            for p in datos_prueba():
                cola.encolar(p)
            print("[+] Lote de 5 pasajeros de prueba cargado a la cola.")

        else:
            print("[!] Opción inválida. Intente nuevamente.")

        pausar()


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    pila_pasajeros = MiPila(10)
    cola_pasajeros = MiCola(10)

    opciones_principales = [
        "0. Salir del programa",
        "1. Módulo Pila (Atención LIFO)",
        "2. Módulo Cola (Atención FIFO)",
    ]

    while True:
        limpiar_pantalla()
        op = menu("SISTEMA DE GESTIÓN Y EMBARQUE DE PASAJEROS", opciones_principales)
        
        if op == 1:
            menu_pila(pila_pasajeros)
        elif op == 2:
            menu_cola(cola_pasajeros)
        elif op == 0:
            limpiar_pantalla()
            print("Cerrando sesión del sistema. ¡Buen viaje!")
            break
        else:
            print("[!] Opción no reconocida.")
            pausar()


if __name__ == "__main__":
    main()