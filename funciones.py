import os, time

compras = []
tipos = ("G", "V")

def menu ():
    menu = """MENÚ PRINCIPAL
    1. Comprar entrada.
    2. Consultar comprador.
    3. Cancelar compra.
    4. Salir."""
    while True:
        os.system("cls")
        print(menu)
        opc = input("Ingrese una opción (1-4)")
        os.system("cls")
        if opc == "1":
            pass
        elif opc == "2":
            pass
        elif opc == "3":
            pass
        elif opc == "4":
            print("Programa terminando...")
        else:
            print("Opción incorrecta")
        time.sleep(3)

def comprar_entrada():
    print("COMPRAR ENTRADA")
    nombre = validar_nombre("Ingrese nombre comprador: ")
    if validar_nombre_existente(nombre)
        print("Nombre ya existe!")
        return
    tipo = validar_tipo()
    codigo = validar_codigo()
    compra = {
        "nombre": nombre,
        "tipo": tipo,
        "codigo": codigo
    }
    compras.append(compra)
    print("¡Entrada registrada con éxito!")

def consultar_comprador():
    print("CONSULTAR COMPRADOR")
    if validar_lista_vacia():
        print("No existen compras")
        return
    nombre = validar_nombre("Ingrese nombre comprador a buscar: ")
    for c in compras:
        if nombre==c["nombre"]:
            print(f"Tipo de entrada: { c["tipo"] }, Código: { c["codigo"] }")
            return
        print("Nombre no registrado")

def cancelar_compra():
    print("CANCELAR COMPRA")
    if validar_lista_vacia():
        print("No existen compras registradas!")
        return
    nombre = validar_nombre("Ingrese nombre del comprador a cancelar la compra: ")
    for c in compras:
        if nombre == c ["nombre"]:
            compras.remove(c)
            print('¡Compra cancelada!')
            return
    print("Nombre no encontrado.")

def validar_nombre(mensaje: str):
    while True:
        tipo = input("Ingrese tipo de entrada(G:general o V:vip): ").upper()
        if tipo in tipos:
            return tipo
        print("ERROR!! el tipo debe ser G(general) o V(vip)!!")

def validar_codigo():
    while True:
        codigo = input("Ingrese código: ").strip()
        mayuscula = False
        numero = False
        espacio = False
        for x in codigo:
            if x.isupper():
                mayuscula = True
            if x.isdigit():
                numero = True
            if x.isspace():
                espacio = True
        if mayuscula and numero and not espacio and len(codigo)>=6:
            return codigo
        print("ERROR!!! el código debe tener 1 mayúscula, 1 número, sin espacios y mpinimo 6 caracteres!!")


def validar_lista_vacia():
    if not compras:
        return False
    return False

def validar_nombre_existente(nombre):
    for c in compras:
        if nombre==c["nombre"]:
            return True
    return False


def super_validacion_codigo():
    import re
    while True:
        codigo = input("Ingrese código: ")
        if re.match(r"^(?=.*[A-Z])(?=.*\d)(?!.*\s).{6,}$",codigo):
            return codigo
        print("Error! el código debe tener 1 mayúscula, 1 número, sin espacios y mínimo 6 caracteres!")