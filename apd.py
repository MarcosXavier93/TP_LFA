import json
import sys
import os
#import keyword
#from pynput.keyboard import Key, Controller

#keyboard = Controller()
#x = 0;
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
            inicial=data['ap'][4]
            final=data['ap'][5]
            global atual
            atual=inicial

            if '#' not in simbolo: #add lambda ao alfabeto de simbolos
                simbolo.append('#')
            if '#' not in alfa_pilha: #add lambda ao topo da pilha
                alfa_pilha.append('#')    

            #print(estado)
            #print(simbolo)
            print(alfa_pilha)
            #print(transicao)
            #print(inicial)
            #print(final)

            entrada=teclado() #entradas teclado

            if checkAlfabeto(entrada,simbolo):
                transicoes(entrada,transicao)
            else:
                print('Não')


        def teclado():#Recebe A Entrada vindo do teclado como :00,01, 00011 ,etc
            entrada = list(input())
            return entrada

        def checkAlfabeto(alfabeto_entrada,alfabeto_simbolo):#Verifica se o que foi digitado pertence ao alfabeto
            for i in alfabeto_entrada:
                if i not in alfabeto_simbolo:
                    return False
            return True

        def checkPilha():
            if len(pilha) == 0:
                return True
            else:
                return False

        def calculo(alfabeto_entrada,alf_transicao):
            if alfabeto_entrada in alf_transicao[1]:
                if alf_transicao[2] != '#':
                    pilha.remove(alf_transicao[2])
                if alf_transicao[4] != '#':
                    str = list(alf_transicao[4])
                    for i in str:
                        pilha.append(i)

        def transicoes(alfabeto_entrada,alf_transicao):
            global atual
            alfabeto_entrada.append('#')
            for j in alfabeto_entrada:
                for i in alf_transicao:
                    if checkPilha():
                        if j in i[1] and atual in i[0]:
                            #print(i)
                            calculo(j,i)
                            atual=i[3]
                            print(pilha)
                            break
                    else:
                        if j in i[1] and atual in i[0] and pilha[0] in i[2]:
                            #print(i)
                            calculo(j,i)
                            atual=i[3]
                            print(pilha)
                            break
            if checkPilha():
                print('Sim')
            else:
                print('Não')

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