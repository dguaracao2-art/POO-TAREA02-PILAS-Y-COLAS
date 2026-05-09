class Pila:
    def __init__(self):
        self.__elementos = []

    def push(self, elemento):
        self.__elementos.append(elemento)

    def pop(self):
        return self.__elementos.pop() if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.__elementos) == 0

    def top(self):
        return self.__elementos[-1] if not self.isEmpty() else None

    def size(self):
        return len(self.__elementos)

    def reverse(self):
        nueva = Pila()
        nueva.__elementos = self.__elementos[::-1]
        return nueva

    def pushAll(self, otraPila):
        self.__elementos.extend(otraPila._Pila__elementos)