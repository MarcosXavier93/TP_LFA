import json
import sys
import os

# import keyword
# from pynput.keyboard import Key, Controller
while True:

    try:
        estado = []  # lista de estados
        simbolo = []  # alfabeto
        alfa_pilha = []  # alfabeto da pilha
        transicao = []  # lista de transicoes
        inicial = ''  # estado inicial
        final = []  # estados finais
        pilha = []  # pilha para manipulacao
        atual = ''  # estado presente


        def start():
            # separando informações do .json
            estado = data['ap'][0]

            simbolo = data['ap'][1]

            alfa_pilha = data['ap'][2]

            transicao = data['ap'][3]
            simbolo_inicial = data['ap'][3][0][2]
            primeiro = data['ap'][3][0][1]
            inicial = data['ap'][4]
            final = data['ap'][5]
            global atual, fim
            atual = inicial
            fim = final

            if '#' not in simbolo:  # add lambda ao alfabeto de simbolos
                simbolo.append('#')
            # if '#' not in alfa_pilha: #add lambda ao topo da pilha
            # alfa_pilha.append('#')

            # print(estado)
            # print(simbolo)
            # print(alfa_pilha)
            # print(transicao)
            # print(inicial)
            # print(final)

            entrada = teclado()  # entradas teclado
            tamanho = len(entrada)
            if checkAlfabeto(entrada, simbolo):
                transicoes(entrada, transicao,simbolo_inicial,primeiro,tamanho)
            else:
                print('Não')


        def teclado():  # Recebe A Entrada vindo do teclado como: 00,01, 00011 ,etc
            entrada = (input())
            entrada = entrada.replace("#", "")
            return entrada


        def checkAlfabeto(alfabeto_entrada, alfabeto_simbolo):  # Verifica se o que foi digitado pertence ao alfabeto
            for i in alfabeto_entrada:
                if i not in alfabeto_simbolo:
                    return False
            return True


        def checkPilha():
            if len(pilha) == 1 and pilha[-1] == '#':
                return True
            else:
                return False


        def calculo(alfabeto_entrada, alf_transicao):
            print('Pilha antes das operacoes',pilha)
            print('entrada ',alfabeto_entrada)
            try:
                pilha.remove('#')  # remover # adicionado anteriormente
            except:
                pass
            if alf_transicao[2] != '#':  # para evitar desempilhar quando não precisa desempilhar
                pilha.pop()  # desempilha quem está no topo da pilha
            if alf_transicao[4] != '#':
                str = list(alf_transicao[4])
                str.reverse()  # inverte lista para empilhar da direita para esquerda
                for i in str:
                    pilha.append(i)
            print('Pilha depois das operacoes',pilha)


        def transicoes(alfabeto_entrada, alf_transicao,simbolo_inicial,primeiro,tamanho):
            global atual, fim
       
            contador = 0
            alfabeto_entrada+='#'
            pilha.append(simbolo_inicial)  # Pilha Comeca Vazia,# significa vazio
            print('Mostrando a pilha', pilha)
            
            
            for j in alfabeto_entrada:
                # if j == '#':#Caso digite # pula para o proximo caracter
                #    break
                for i in alf_transicao:
                    # print(j, atual, pilha[-1])
                    if (j in i[1] and atual in i[0] and pilha[-1] in i[2]) or (j in i[1] and atual in i[0] and '#' in i[2]):  # topo da pilha existe na transição para desempilhar
                    
                        calculo(j, i)
                        atual = i[3]
                        if len(pilha) == 0:  # pilha vazia coloca lambda pra marcar
                            pilha.append(simbolo_inicial)
                        break
                    else:
                        contador = contador + 1
                if contador == len(alf_transicao):  # não existe transição para o simbolo
                    pilha.append('#')  # so para pilhar ter tamanho >1
                    break;
                else:
                    contador = 0
                if len(pilha) == 1 and pilha[-1] == 'F':  # SE TIVER 1 SO ELEMENTO na pilha e ele for F (FUNDO)
                    save = j
                    j = '#'
                    for i in alf_transicao:
                        if j in i[1] and atual in i[0] and pilha[-1] in i[2]:  # a pilha não está vazia e topo da pilha existe na transição para desempilhar
                            
                            calculo(j, i)
                            atual = i[3]
                            break
                    j = save
                    pilha.append('#')  # marcar que a pilha esta vazia
            
            
            if  atual in fim :  # confere se pilha esta vazia e se estado atual existe como estado final
                print('Sim')
                print('atual',atual)
                print("Pilha final: ",pilha)
                print("estado: ", atual)
            else:
                print('Não')
                print('atual',atual)
                print("Pilha final: ",pilha)
                # print("estado: ", atual)

        path = sys.argv[1]
        if os.path.exists(path):
            f = open(path, )
            data = json.load(f)
            f.close
            start()
        else:
            print('Arquivo não encontrado')
    except (EOFError, KeyboardInterrupt) as e:
        sys.exit(0)