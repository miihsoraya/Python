print("-----------------------------------------------------\n")

print("|        Programa  para transformacao de:           |\n")

print("|                AFN para AFD                       |\n")

print("-----------------------------------------------------\n")

afn = {}
n = int(input("Nº. de estados : "))  # exemplo: A, B, C, D
t = int(input("Nº. de transações : "))  # exemplo: a,b,c Alfabeto
if n<5:
    for i in range(n):
        state = input("Nome do estado : ")  #  A, B, C, q1, q2 ..etc
        afn[state] = {}  # dicionario . a chave sao os estados
        for j in range(t):
            simb = input("Símbolo do alfabeto : ")  # Enter path eg : a or b in {a,b} 0 or 1 in {0,1}
            print("Digite o estado final de {} viajando pelo caminho {} : ".format(state, simb))
            atingiuState = [x for x in input().split()]  # coloca quebrado os estados finais de cada simbolo
            afn[state][simb] = atingiuState  #inclue em cada simbolo digitado os estados finais referentes
        #print(len(afn[state][simb][atingiuState]))
    print("\nNFA :- \n")
    print(afn)  # Printing NFA


    print("Digite o estado final : ")
    afn_final_state = [x for x in input().split()]
    ###################################################

    new_states_list = []  # os novos estados
    afd = {}  # imprimir dicionario depois
    keys_list = list(list(afn.keys())[0])  # contem todos os estados do nfa + os criados no dfa
    simb_list = list(afn[keys_list[0]].keys())  # lista todos os caminhos dos simbolos: [a,b]

    ###################################################

    afd[keys_list[0]] = {}  # novo dicionario afd
    for y in range(t): #transicoes
        var = "".join(afn[keys_list[0]][     #JOIN separa nomes e coloca o "" juntando estados
                          simb_list[y]])     # criar uma unica sequencia a partir de todos os elementos da lista

        afd[keys_list[0]][simb_list[y]] = var  # colocando os estados referentes ao AFD
        if var not in keys_list:  # se o estado é novo, ele deve ser colocado com key A: B: AB:
            new_states_list.append(var)  # entao ele é incluido
            keys_list.append(var)  # keys_list contem todos os estados

    ###################################################
    while len(new_states_list) != 0:  # apenas se o new_states_list nao esta vazio
        afd[new_states_list[0]] = {}  # toma o primeiro elemento de new_states_list e analisa
        for _ in range(len(new_states_list[0])):
            for i in range(len(simb_list)):
                temp = []  # criando lista temporaria
                for j in range(len(new_states_list[0])):
                    temp += afn[new_states_list[0][j]][simb_list[i]]  # unindo os estados
                s = ""
                s = s.join(temp)  # criando string simples(novo estado) de todos os elementos da list
                if s not in keys_list:  # se o estado é novo
                    new_states_list.append(s)  # entao inclue
                    keys_list.append(s)
                afd[new_states_list[0]][simb_list[i]] = s  # assigning the new state in the DFA table

        new_states_list.remove(new_states_list[0])  # Removendo o primeiro elemento de new_states_list

    print("\nDFA :- \n")
    print(afd)


    afd_states_list = list(afd.keys())
    afd_final_states = []
    for x in afd_states_list:
        for i in x:
            if i in afn_final_state: #se keys estao no afd_final_state
                afd_final_states.append(x) #adiciona os estados finais
                break

    print("\nEstados Finais do AFD são : ", afd_final_states)  # Printing Final states of DFA
