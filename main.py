from arbol import Arbol

def mostrar_menu():
    print("Opciones:")
    print("1. Agregar personaje")
    print("2. Buscar personaje")
    print("3. Eliminar personaje")
    print("4. Mostrar recorridos")
    print("5. Salir")

# Crear el árbol con algunos personajes
arbol = Arbol("Dungeon")
arbol.agregar("Guerrero")
arbol.agregar("Cazadora")
arbol.agregar("Ladrón")
arbol.agregar("Mago")

opcion = 0

while opcion != 5:
    mostrar_menu()
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            personaje = input("Ingrese el nombre del personaje a agregar: ")
            arbol.agregar(personaje)
            print(f"Personaje '{personaje}' agregado al árbol.")
        elif opcion == 2:
            personaje_buscar = input("Ingrese el nombre del personaje a buscar: ")
            nodo_encontrado = arbol.buscar(personaje_buscar)
            if nodo_encontrado:
                print(f"El personaje '{personaje_buscar}' está en el árbol.")
            else:
                print(f"El personaje '{personaje_buscar}' no está en el árbol.")
        elif opcion == 3:
            personaje_eliminar = input("Ingrese el nombre del personaje a eliminar: ")
            arbol.eliminar(personaje_eliminar)
            print(f"Personaje '{personaje_eliminar}' eliminado del árbol.")
        elif opcion == 4:
            print("Recorridos:")
            arbol.preorden()
            arbol.inorden()
            arbol.postorden()
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Ingrese un número del 1 al 5.")
    except ValueError:
        print("Por favor, ingrese un número.")

