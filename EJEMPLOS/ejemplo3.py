from collections import deque

# Crear una cola
cola = deque()

# Agregar elementos a la cola
cola.append('Elemento 1')
cola.append('Elemento 2')
cola.append('Elemento 3')

print("Estado de la cola:", cola)

# Quitar un elemento de la cola
primer_elemento = cola.popleft()
print("Se ha quitado:", primer_elemento)

print("Estado de la cola después de quitar un elemento:", cola)

# Agregar otro elemento
cola.append('Elemento 4')
print("Estado de la cola después de agregar otro elemento:", cola)
```
