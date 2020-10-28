import json
import sys
import os
#import keyword
#from pynput.keyboard import Key, Controller
while True:
    
    try:
        estado = [] #lista de estados
        simbolo = []  # alfabeto
        alfa_pilha = []  # alfabeto da pilha
        transicao = [] #lista de transicoes
        inicial = ''  # estado inicial
        final = []  # estados finais
        pilha = [] #pilha para manipulacao
        atual = '' #estado presente

        def start():
            #separando informações do .json
            estado = data['ap'][0]
            
            simbolo = data['ap'][1]
            
            alfa_pilha = data['ap'][2]
            
            transicao=data['ap'][3]
            inicial = data['ap'][4]
            final=data['ap'][5]
            global atual
            atual=inicial

            if '#' not in simbolo: #add lambda ao alfabeto de simbolos
                simbolo.append('#')
            #if '#' not in alfa_pilha: #add lambda ao topo da pilha
                #alfa_pilha.append('#')    

            #print(estado)
            #print(simbolo)
            #print(alfa_pilha)
            #print(transicao)
            #print(inicial)
            #print(final)

            entrada=teclado() #entradas teclado

            if checkAlfabeto(entrada,simbolo):
                transicoes(entrada,transicao)
            else:
                print('Não')


        def teclado():#Recebe A Entrada vindo do teclado como: 00,01, 00011 ,etc
            entrada = list(input())
            return entrada

        def checkAlfabeto(alfabeto_entrada,alfabeto_simbolo):#Verifica se o que foi digitado pertence ao alfabeto
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
            pilha.pop() #desempilha quem está no topo da pilha
            if alf_transicao[4] != '#':
                str = list(alf_transicao[4])
                str.reverse() #inverte lista para empilhar da direita para esquerda
                for i in str:
                    pilha.append(i)
            print('Pilha depois das operacoes',pilha)
        def transicoes(alfabeto_entrada,alf_transicao):
            global atual
            #alfabeto_entrada.append('#')
            pilha.append('#')  #Pilha Comeca Vazia,# significa vazio 
            print('Mostrando a pilha',pilha)
            for j in alfabeto_entrada:
                #if j == '#':#Caso digite # pula para o proximo caracter
                #    break
                for i in alf_transicao:
                    if j in i[1] and atual in i[0] and pilha[-1] in i[2]: # pilha não está vazia e topo da pilha existe na transição para desempilhar
                        print("A")
                        calculo(j,i)
                        atual=i[3]
                        break
                if len(pilha) == 1 and pilha[-1] == 'F': #SE TIVER 1 SO ELEMENTO na pilha e ele for F
                    save = j
                    j = '#'
                    for i in alf_transicao:
                        if j in i[1] and atual in i[0] and pilha[-1] in i[2]:  # pilha não está vazia e topo da pilha existe na transição para desempilhar
                            print("B")
                            calculo(j, i)
                            atual = i[3]
                            break
                    j=save
                    pilha.append('#')
            if checkPilha():
                print('Sim')
                print("Pilha final: ",pilha)
            else:
                print('Não')
                print("Pilha final: ",pilha)

        path = sys.argv[1]
        if os.path.exists(path):
            f = open(path,)
            data = json.load(f)
            f.close
            start()
        else:
            print('Arquivo não encontrado')
    except (EOFError, KeyboardInterrupt) as e:
        sys.exit(0)