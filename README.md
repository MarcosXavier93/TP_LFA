# TP_LFA
Implementar um programa que verifica se pertence ou nao a uma linguagem

Dupla : Alan e Marcos Junio

## Bibliotecas Utilizadas
Json,sys,os
Para instalar essas bibliotecas do Python:
pip install json
pip install os
pip install sys
## Como rodar o Programa

 Ao fazer o clone da pasta, abrir o terminal e digitar python apd.py exemplo.json (talvez seja necessario digitar python3 apd.py exemplo.json) ,onde exemplo.json contem todas informacoes do automato de pilha,como exemplo:


 { "ap": [
 ["0", "1", "f"],
 ["0", "1", "t"],
 ["X"],
 [
 ["0", "0", "#", "0", "X"],
 ["0", "1", "X", "1", "#"],
 ["0", "t", "#", "f", "#"],
 ["f", "#", "X", "f", "#"],
 ["1", "t", "#", "f", "#"],
 ["1", "1", "X", "1", "#"]
 ],
 "0",
 ["f"]
]}

