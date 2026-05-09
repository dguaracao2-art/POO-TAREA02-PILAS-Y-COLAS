class Cola:
    def __init__(self):
        self.__elementos = []

    def push(self, elemento):
        self.__elementos.append(elemento)

    def pop(self):
        return self.__elementos.pop(0) if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.__elementos) == 0

    def top(self):
        return self.__elementos[0] if not self.isEmpty() else None

    def size(self):
        return len(self.__elementos)

    def reverse(self):
        nueva = Cola()
        nueva.__elementos = self.__elementos[::-1]
        return nueva

    def pushAll(self, otraCola):
        self.__elementos.extend(otraCola._Cola__elementos)