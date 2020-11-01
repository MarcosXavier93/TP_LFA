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
            simbolo_inicial=data['ap'][3][0][2]
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

            if checkAlfabeto(entrada, simbolo):
                transicoes(entrada, transicao,simbolo_inicial)
            else:
                print('Não')


        def teclado():  # Recebe A Entrada vindo do teclado como: 00,01, 00011 ,etc
            entrada = (input())
            entrada = entrada.replace("#", "") # lambda faz parte da palavra
            entrada = entrada+'#'
            return entrada


        def checkAlfabeto(alfabeto_entrada, alfabeto_simbolo):  # Verifica se o que foi digitado pertence ao alfabeto
            for i in alfabeto_entrada:
                if i not in alfabeto_simbolo:
                    return False
            return True


        def checkPilha():
            global pilha
            if len(pilha) == 0:# and pilha[-1] == '#':
                return True
            else:
                return False


        def calculo(alfabeto_entrada, alf_transicao):
            global pilha
            # print('Pilha antes das operacoes',pilha)
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
            # print('Pilha depois das operacoes',pilha)

        def passo2(transicoes_encontrada):
            global pilha
            for i in transicoes_encontrada:
                try:
                    if (pilha[-1] in i[2] or i[2] == '#'):  # encontrar transicao que está desempilhando topo da pilha ou desempilhando nada
                        transicoes_encontrada.clear()  # remove todas transicoes encontradas
                        transicoes_encontrada = transicoes_encontrada + [i]  # adiciona transicao correta
                except:
                    pilha.append(i[2])
                    if (pilha[-1] in i[2] or i[2] == '#'):  # encontrar transicao que está desempilhando topo da pilha ou desempilhando nada
                        transicoes_encontrada.clear()  # remove todas transicoes encontradas
                        transicoes_encontrada = transicoes_encontrada + [i]  # adiciona transicao correta
            if (len(transicoes_encontrada) > 1):  # não escolheu nenhuma transição adequada das encontradas
                transicoes_encontrada.clear()
            return transicoes_encontrada

        def passo1(simbolo_atual,alf_transicao,transicoes_encontrada):
            global atual
            for i in alf_transicao:  # percorrer transicoes
                if (atual in i[0] and simbolo_atual in i[1]):  # se encontrar transicao em que estado atual e simbolo atual estão presentes
                    transicoes_encontrada = transicoes_encontrada+[i]  # guardar essa transicao
            print('Encontrou: ',transicoes_encontrada)
            print(len(transicoes_encontrada))
            if (len(transicoes_encontrada) > 1):  # se tiver mais de uma transicao com estado atual e simbolo atual presente
                transicoes_encontrada = passo2(transicoes_encontrada)
            return transicoes_encontrada

        def procuraTransicao(simbolo_atual, alf_transicao, transicoes_encontrada):
            global atual, flag, pilha
            transicoes_encontrada=passo1(simbolo_atual,alf_transicao,transicoes_encontrada)
            if (len(transicoes_encontrada) == 0):  # nao foi encontrado transicoes
                print('entrou')
                simbolo_atual = '#'
                flag = False #marcar que já tentou de tudo para achar
                transicoes_encontrada=passo1(simbolo_atual,alf_transicao,transicoes_encontrada)
            print('Escolhida: ', transicoes_encontrada)
            return transicoes_encontrada

        def transicoes(alfabeto_entrada, alf_transicao,simbolo_inicial):
            global atual, fim, flag, pilha, resultado
            flag = True
            resultado = False
            transicoes_encontrada=[]
            j = 0
            print('tamanho:',len(alfabeto_entrada))
            while j < len(alfabeto_entrada):
                print('pilha: ',pilha)
                print('alfabeto entrada:',alfabeto_entrada[j])
                print(j)
                transicoes_encontrada=procuraTransicao(alfabeto_entrada[j],alf_transicao, transicoes_encontrada)
                if(len(transicoes_encontrada)>0):
                    if(transicoes_encontrada[0][2] != '#' and checkPilha() and transicoes_encontrada[0][1] != '#'):
                        resultado=False
                        break
                    elif(transicoes_encontrada[0][1]=='#' and checkPilha() and transicoes_encontrada[0][2] != '#'): #lê nada, desempilha algo e pilha já está vazia
                        resultado=True
                        break
                    elif(transicoes_encontrada[0][2] != '#' and not(transicoes_encontrada[0][2] in pilha[-1]) and transicoes_encontrada[0][1] != '#'):
                        resultado = False
                        break
                    else:
                        calculo(alfabeto_entrada[j], transicoes_encontrada[0])
                        atual = transicoes_encontrada[0][3]
                        transicoes_encontrada.clear()
                    if(j == (len(alfabeto_entrada)-1) and checkPilha() and atual in fim):
                        resultado=True
                        #print('Sim')
                    else:
                        resultado=False
                    if flag:
                        j=j+1
                    else:
                        flag=True
                elif checkPilha() and atual in fim and not flag and alfabeto_entrada[j]=='#':
                    resultado=True
                    break
                else:
                    resultado=False
                    break

            if resultado:
                print('Sim')
            else:
                print('Não')
                print('atual',atual)
                print('flag',flag)

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