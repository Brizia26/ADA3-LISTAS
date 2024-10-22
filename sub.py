class Nodo:
    """Clase que representa un nodo de la lista enlazada."""
    def __init__(self, postre, ingredientes):
        self.postre = postre
        self.ingredientes = ingredientes
        self.siguiente = None

class ListaEnlazada:
    """Clase que representa una lista enlazada de postres."""
    def __init__(self):
        self.cabeza = None

    def agregar_postre(self, postre, ingredientes):
        """Agrega un nuevo postre a la lista."""
        nuevo_nodo = Nodo(postre, sorted(ingredientes))  
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"Postre '{postre}' añadido con ingredientes: {nuevo_nodo.ingredientes}.")

    def mostrar_postres(self):
        """Muestra todos los postres y sus ingredientes en orden alfabético."""
        if self.cabeza is None:
            print("No hay postres disponibles.")
            return
        actual = self.cabeza
        postres_lista = []
        while actual:
            postres_lista.append((actual.postre, actual.ingredientes))
            actual = actual.siguiente

        postres_lista.sort(key=lambda x: x[0])
        for postre, ingredientes in postres_lista:
            print(f"- {postre}: {ingredientes}")

    def eliminar_duplicados(self):
        """Elimina los postres repetidos de la lista enlazada."""
        if self.cabeza is None:
            return
        actual = self.cabeza
        prev = None
        vistos = set()
        while actual:
            if actual.postre in vistos:
                prev.siguiente = actual.siguiente  # Elimina el nodo duplicado
                print(f"Postre duplicado '{actual.postre}' eliminado.")
            else:
                vistos.add(actual.postre)
                prev = actual
            actual = actual.siguiente

    def buscar_postre(self, nombre_postre):
        """Busca un postre y retorna su nodo."""
        actual = self.cabeza
        while actual:
            if actual.postre == nombre_postre:
                return actual
            actual = actual.siguiente
        return None

    def eliminar_postre(self, nombre_postre):
        """Elimina un postre de la lista."""
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.postre == nombre_postre:
                if anterior is None: 
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                print(f"Postre '{nombre_postre}' eliminado.")
                return
            anterior = actual
            actual = actual.siguiente
        print("El postre no existe.")

    def agregar_ingrediente(self, nombre_postre, ingrediente):
        """Agrega un ingrediente a un postre existente."""
        nodo = self.buscar_postre(nombre_postre)
        if nodo:
            nodo.ingredientes.append(ingrediente)
            nodo.ingredientes.sort()  
            print(f"Ingrediente '{ingrediente}' añadido al postre '{nombre_postre}'.")
        else:
            print("El postre no existe.")

    def eliminar_ingrediente(self, nombre_postre, ingrediente):
        """Elimina un ingrediente de un postre existente."""
        nodo = self.buscar_postre(nombre_postre)
        if nodo:
            if ingrediente in nodo.ingredientes:
                nodo.ingredientes.remove(ingrediente)
                print(f"Ingrediente '{ingrediente}' eliminado del postre '{nombre_postre}'.")
            else:
                print(f"El ingrediente '{ingrediente}' no se encontró en el postre '{nombre_postre}'.")
        else:
            print("El postre no existe.")

def menu(lista_enlazada):
    while True:
        print("\n--- Menú de Postres ---")
        print("1. Mostrar todos los postres")
        print("2. Ver ingredientes de un postre")
        print("3. Agregar ingrediente a un postre")
        print("4. Eliminar ingrediente de un postre")
        print("5. Agregar un nuevo postre")
        print("6. Eliminar un postre")
        print("7. Eliminar postres duplicados")
        print("8. Salir")
        
        opcion = input("Elija una opción: ")

        if opcion == "1":
            lista_enlazada.mostrar_postres()

        elif opcion == "2":
            nombre_postre = input("Ingrese el nombre del postre: ")
            nodo = lista_enlazada.buscar_postre(nombre_postre)
            if nodo:
                print(f"Ingredientes de {nombre_postre}: {nodo.ingredientes}")
            else:
                print("El postre no existe.")
        
        elif opcion == "3":
            nombre_postre = input("Ingrese el nombre del postre: ")
            ingrediente = input("Ingrese el ingrediente a agregar: ")
            lista_enlazada.agregar_ingrediente(nombre_postre, ingrediente)
        
        elif opcion == "4":
            nombre_postre = input("Ingrese el nombre del postre: ")
            ingrediente = input("Ingrese el ingrediente a eliminar: ")
            lista_enlazada.eliminar_ingrediente(nombre_postre, ingrediente)
        
        elif opcion == "5":
            nombre_postre = input("Ingrese el nombre del nuevo postre: ")
            ingredientes = []
            while True:
                ingrediente = input("Ingrese un ingrediente: ")
                if ingrediente.lower() == 'salir':
                    break
                ingredientes.append(ingrediente)
            lista_enlazada.agregar_postre(nombre_postre, ingredientes)
        
        elif opcion == "6":
            nombre_postre = input("Ingrese el nombre del postre a eliminar: ")
            lista_enlazada.eliminar_postre(nombre_postre)

        elif opcion == "7":
            lista_enlazada.eliminar_duplicados()

        elif opcion == "8":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    print("Bienvenido al gestor de postres.")
    lista_enlazada = ListaEnlazada()

    menu(lista_enlazada)
