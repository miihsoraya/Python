minha_lista=['Iron', 200, 'ola', False, [], -1, 150]

'''1ª letra'''
minha_lista.extend(('almoco',200))
print(minha_lista)

'''2ª letra'''
minha_lista.insert(2, 'unicornio')
print(minha_lista)

'''3ª letra'''
minha_lista.insert(0,2018)
print(minha_lista)

'''4ª letra'''
print(minha_lista.index('ola'))

'''5ª letra'''
print(minha_lista.count(200))

'''6ª letra'''
minha_lista.remove(200)
print(minha_lista)
