class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("Desapilando de una pila vacía")

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")

    def size(self):
        return len(self.items)

# Ejemplo de uso de la pila
if __name__ == "__main__":
    pila = Pila()
    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)

    print("Elemento en la parte superior de la pila:", pila.peek()) # Debe mostrar 3
    print("Desapilando:", pila.desapilar()) # Debe mostrar 3
    print("¿Está la pila vacía?", pila.esta_vacia()) # Debe mostrar False
    print("Tamaño de la pila:", pila.size()) # Debe mostrar 2
