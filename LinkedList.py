
                                       ### EM CONSTRUÇÃO ####

from teste2 import Node


class LinkedList:
    def __init__(self):
        self.head = None #cabeca
        self._size = 0 #por segurança

    def append(self, elem):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head #aponta ao longo da sequencia de nós
            while(pointer.next): #enquanto next for igual a True // percorrer lista
                pointer = pointer.next
            pointer.next = Node(elem) #quando chegar ao ultimo, insere o elem
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range") #return None
        return pointer

    def __getitem__(self, index): #prevendo um comprtamento "sobrecarga de operador"
        # a = lista[6]
        pointer = self._getnode(index)
        if pointer:#nao for None
            return pointer.data #verificar se esta no vazio
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        # lista[5] = 9 Modificar valor
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem):
        """Retorna o índice do elem na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem: #se o dado desse nó é igual ao q estou procurando
                return i
            pointer = pointer.next
            i = i+1
        return ValueError("{} não esta na lista".format(elem))

    def insert(self, index, elem):
        node = Node(elem) #recebe o elemento(dado)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1

    def remove(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True
        raise ValueError("{} is not in list".format(elem))

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    # sequencial = []
    # sequencial.append(7)
    lista = LinkedList()
    lista.append(7)
    lista.append(80)
    lista.append(56)
    lista.append(32)
    lista.append(17)
    print(lista.__len__())
    print(lista.index(58))
    print(lista.__str__())
    print(lista.__getitem__(2))
