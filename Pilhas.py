class Pilha:
    def __init__(self):
        self.items=[]
    def empilhar(self,valor):
        self.items.append(valor)
    def desempilhar(self):
        self.items.pop()
    def vazia(self):
        if self.tamanho() == 0:
            return True
        else:
            return False
    def topo(self):
        return self.items[-1]
    def tamanho(self):
        return len(self.items)
    def fim(self):
        return self.items[-(self.tamanho())]
   
p = Pilha()
p.empilhar(6)
p.empilhar(2)
p.empilhar(4)

print(p.vazia())
print(p.topo())
print(p.tamanho())
print(p.fim())

for i in range(3):
    p.desempilhar()

