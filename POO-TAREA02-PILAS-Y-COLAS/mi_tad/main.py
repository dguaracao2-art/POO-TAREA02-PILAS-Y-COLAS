from modelo.pila import Pila
from modelo.cola import Cola

print("=" * 50)
print("   TAD PILA — Comportamiento LIFO")
print("=" * 50)

pila = Pila()

pila.push(10)
pila.push(20)
pila.push(30)

print(pila.contiene(20))
print(pila.contiene(99))
print(pila)


cola = Cola()
cola.push("A")
cola.push("B")
cola.push("C")

print(f"Cola inicial:     {cola}")
print(f"Frente (top):     {cola.top()}")
print(f"Extrae (pop):     {cola.pop()}")
print(f"Cola luego pop:   {cola}")
print(f"Tamaño (size):    {cola.size()}")
print(f"¿Vacía?:          {cola.isEmpty()}")

cola2 = Cola()
cola2.push("X")
cola2.push("Y")
cola.pushAll(cola2)
print(f"Luego pushAll:    {cola}")

invertida_cola = cola.reverse()
print(f"Cola invertida:   {invertida_cola}")