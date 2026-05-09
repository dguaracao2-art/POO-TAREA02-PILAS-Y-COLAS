from modelo.pila import Pila
from modelo.cola import Cola
from faker import Faker

# Inicializamos Faker
fake = Faker()

def ejecutar_prueba():
    mi_pila = Pila()
    mi_cola = Cola()

    print("--- Generando datos aleatorios con Faker ---")
    for _ in range(5):
        nombre = fake.name()
        mi_pila.push(nombre)
        mi_cola.push(nombre)
        print(f"Insertando: {nombre}")

    print(f"\n[PILA] El último en entrar fue: {mi_pila.top()}")
    print(f"[COLA] El primero en entrar fue: {mi_cola.top()}")

if __name__ == "__main__":
    ejecutar_prueba()