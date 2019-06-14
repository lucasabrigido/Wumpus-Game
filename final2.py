''' 
O = Andável 
Y = Protagonista 
M = Monstro 
V = Brisa 
F = Fedor 
@ = Ouro 
P = Porta 
B = Buraco 
R = Rocha 
'''
from random import randint 
import os
from os.path import exists
import time
from msvcrt import getch
from pygame import mixer
def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')
def print_h(texto):
    for i in range(len(texto) + 1):
        limpa()
        print(texto[:i])
        time.sleep(0.015)
def musica(song):
    mixer.init()
    if song == 'intro':
        mixer.music.load('inazuma.ogg')
    if song == 'dungeon':
        print_h('Eu - Sorte que eu trouxe meu MP3, esse brinquedo deve ser um tédio,que tipo de som devo escolher ? \n 1 - Naruto \n 2 - Ciro falando sobre astrofísica \n 3 - Inazuma Eleven \n 4 - Garçom ')
        music = int(input())
        lista_music = ['naruto.ogg','ciro.ogg','inazuma2.ogg','garcom.ogg']
        mixer.music.load(lista_music[music-1])
    if song == 'fim':
        mixer.music.load('yuri.ogg')
    mixer.music.play(-1)
musica('intro')
print_h("Moça Aleatória - Bem Vindo ao mundo de Wumpus! Gostaria de testar nossa mais nova atração do park?! Há boatos que todos que jogaram se assustaram tanto que saíram correndo de medo, HAHAHA ")
começar = input().upper()
frases = ["Eu: Claro que eu quero testar,-Bem vindo ao mundo de Wumpus-, até parece que um brinquedo desse iria me assustar, está tudo muito escuro, vamos ver o que o manual de instrução diz sobre o jogo, parece um mapa ? Ele me mostra: ", "Y - Você, M - Monstro, B - Buraco, @ - Ouro, P - Porta, V - Briza, F - Fedor, O - Andável, R - Rochas, X - Névoa", "Eu - Estranho, nem todos estão visíveis no manual/mapa, apenas eu e a porta, vamos ver o que mais o manual tem a dizer nas entrelinhas","--> Você está em uma dungeon, cuidado! Existem buracos, você pode se machucar de verdade!", "--> Mas não precisa se preocupar, está tudo escuro, porém é possível sentir a briza quando está se aproximando de um bueiro!", "--> Existem ouros escondidos pela dungeon! Mas não seja muito egoísta, Wumpus não gostaria de perder seu bem mais precioso!", "--> Ah, não se preocupe com ele, esse fede tantooooo que qualquer um sentiria a sua presença!", "--> Caso você sinta essa presença, você pode desistir do brinquedo e sair pela porta à hora que desejar ou se divertir o máximo possível e tentar matá-lo, facilitando sua busca por ouro!","--> Não se esqueça, você só tem um tiro! a gerência do parque não se responsabiliza por machucados, boa aventura!","Eu - Isso não me assusta nem um pouco, já me sinto confiante o suficiente para começar, vou escolher o nível... "]
while começar == "SIM":
  for l in range(10):
    print_h(frases[l])
    input()
  limpa()
  for l in range(10): 
    print(frases[l] + '\n' + '\n')
    time.sleep(0.5)
  break
def dificuldade(nivel): 
    m = [] 
    if nivel == "easy": 
        pos = 6 
        ouro = 1 
    if nivel == "medium": 
        pos = 8 
        ouro = 2 
    if nivel == "hard": 
        pos = 12 
        ouro = 3 
    for x in range(pos): 
        m = m + [[['O']]*pos] 
    for k in range(pos): 
        m[k][0] = 'R' 
        m[k][pos-1] = 'R' 
    m[0] = ['R']*pos 
    m[pos-1] = ['R']*pos 
    m[1][1] = ['O','Y'] 
    m[1][0] = 'P' 
    buracos = round(0.18*(pos-2)**2) 
    while buracos != 0: 
        linha = randint(1,pos-2) 
        coluna = randint(1,pos-2) 
        if (linha != 1 or coluna != 1) and (linha != 1 or coluna != 2) and (linha != 2 or coluna != 1) and m[linha][coluna] != 'B':  
            m[linha][coluna] = 'B' 
            buracos -= 1 
            if (m[linha-1][coluna] != 'R' and m[linha-1][coluna] != 'B') and 'V' not in m[linha-1][coluna]: 
                m[linha-1][coluna] = m[linha-1][coluna] + ['V'] 
            if (m[linha+1][coluna] != 'R' and m[linha+1][coluna] != 'B') and 'V' not in m[linha+1][coluna]: 
                m[linha+1][coluna] = m[linha+1][coluna] + ['V'] 
            if (m[linha][coluna-1] != 'R' and m[linha][coluna-1] != 'B') and 'V' not in m[linha][coluna-1]: 
                m[linha][coluna-1] = m[linha][coluna-1] + ['V'] 
            if (m[linha][coluna+1] != 'R' and m[linha][coluna+1] != 'B') and 'V' not in m[linha][coluna+1]: 
                m[linha][coluna+1] = m[linha][coluna+1] + ['V'] 
    while ouro != 0: 
        linha = randint(2,pos-3) 
        coluna = randint(2,pos-3) 
        if (linha != 1 or coluna != 1) and ('@' not in m[linha][coluna] and m[linha][coluna] != 'B'): 
            if (m[linha-1][coluna] != 'B' or m[linha+1][coluna] != 'B') or (m[linha][coluna-1] != 'B' or m[linha][coluna+1] != 'B'): 
                m[linha][coluna] = m[linha][coluna] + ['@'] 
                ouro -= 1 
    monster = 1 
    while monster != 0: 
        linha = randint(1,pos-2) 
        coluna = randint(1,pos-2) 
        if (linha != 1 or coluna != 1) and (linha != 1 or coluna != 2) and (linha != 2 or coluna != 1) and m[linha][coluna] != 'B': 
            m[linha][coluna] = m[linha][coluna] + ['M'] 
            if m[linha-1][coluna] != 'R' and m[linha-1][coluna] != 'B': 
                m[linha-1][coluna] = m[linha-1][coluna] + ['F'] 
            if m[linha+1][coluna] != 'R' and m[linha+1][coluna] != 'B': 
                m[linha+1][coluna] = m[linha+1][coluna] + ['F'] 
            if m[linha][coluna-1] != 'R' and m[linha][coluna-1] != 'B': 
                m[linha][coluna-1] = m[linha][coluna-1] + ['F'] 
            if m[linha][coluna+1] != 'R' and m[linha][coluna+1] != 'B': 
                m[linha][coluna+1] = m[linha][coluna+1] + ['F'] 
            monster -= 1 
    return m 
def elegante(a): 
    for n in a: 
        print(n) 
def movimento(mapa, linha, coluna, pontos):
    dicionario["parar"] = "continuar"
    dicionario["linhaA"] = dicionario['linha']
    dicionario["colunaA"] = dicionario['coluna']
    del mapa[dicionario['linha']][dicionario['coluna']][mapa[dicionario['linha']][dicionario['coluna']].index("Y")]
    if mov == "D":
        dicionario["coluna"] = dicionario['coluna'] + 1
    if mov == "W":       
        dicionario["linha"] = dicionario['linha'] - 1
    if mov == "S":       
        dicionario["linha"] = dicionario['linha']+1
    if mov == "A":       
        dicionario["coluna"] = dicionario['coluna'] - 1        
    nova = mapa[dicionario["linha"]][dicionario["coluna"]]
    mapa[dicionario["linha"]][dicionario["coluna"]] += "Y"
    if "@" in nova and 'M' not in nova:
        dicionario["parar"] = 'ouro'      
    if "M" in nova:
        dicionario["frase"] = "Eu - MEU DEUS, UM MOOOONSTRO!!! Será que ele é de verdade? ISSO CERTAMENTE NÃO É UM BRINQUEDO!!!!"
        dicionario["parar"] = "Break"
        dicionario["pontos"] = dicionario["pontos"] - 10000
    elif "B" in nova: 
        dicionario["frase"] = "Eu - AHHHH NÃO, ESTOU CAINDO! Sorte que é um brin...*pluf*"
        dicionario["parar"] = "Break"
        dicionario["pontos"] = dicionario["pontos"] - 10000         
    elif "P" in nova:
        dicionario["frase"] = "Eu - QUE BRINQUEDO IDIOTA, VOU PROCESSAR ESSA EMPRESA, EU PODERIA TER ME MACHUCADO!"
        dicionario["parar"] = "Break"
        dicionario["pontos"] = dicionario["pontos"] + 1        
    elif "R" in nova:
        mapa[dicionario["linha"]][dicionario["coluna"]] = "R"
        mapa[dicionario["linhaA"]][dicionario["colunaA"]] += "Y"
        dicionario["frase"] = "Eu - Muitas rochas, não consigo passar daqui!"
        dicionario["pontos"] = dicionario["pontos"] + 1
        dicionario["linha"] = dicionario["linhaA"]
        dicionario["coluna"] = dicionario["colunaA"]        
    elif ("V" in nova and "F" in nova) and  "@" in nova:
        dicionario["frase"] = "Eu - Essa mistura de vento e fedor, que nojo. Achei uma barra de ouro! Devo pegar?"      
    elif "V" in nova and "F" in nova:
        dicionario["frase"] = "Eu - Que nojo, essa briza trazendo todo esse fedor"
    elif "V" in nova and "@" in nova:
        dicionario["frase"] = "Eu - Estou sentido uma briza. Olha ouro! Pego ou não pego?"
    elif "F" in nova and "@" in nova:
        dicionario["frase"] = "Eu - Estou sentido um fedor, pelo menos esse ouro aqui alivia a pressão. I pick?"
    elif "F" in nova:
        dicionario["frase"] = "Eu - Que fedooor, melhor eu dar o fora desse lado"
    elif "V" in nova:
        dicionario["frase"] = "Eu - Ventos fortes, talvez seja perigoso seguir em frente"     
    elif "@" in nova:
        dicionario["frase"] = "Eu - UOUUU, OOOURO! Eu pego essa belezura?"       
    elif "O" in nova:
        dicionario["frase"] = "Eu - Que estranho, não vejo nada perto"       
def shoot():
    dir = key
    limpa()
    buffl = 0
    buffc = 0
    if dir == 'U':
        buffl = -1
    if dir == 'H':
        buffc = -1
    if dir == 'J':
        buffl = +1
    if dir == 'K':
        buffc = +1
    tirol = dicionario['linha']
    tiroc = dicionario['coluna']
    while 1 < 2:
        tirol += buffl
        tiroc += buffc
        if mapa[tirol][tiroc] == 'R' or mapa[tirol][tiroc] == 'P':
            break
        if 'M' in mapa[tirol][tiroc]:
            dicionario['pontos'] = dicionario['pontos'] + 10000
            if len(mapa[tirol+1][tiroc]) > 1:
                del mapa[tirol+1][tiroc][mapa[tirol+1][tiroc].index('F')]
            if len(mapa[tirol-1][tiroc]) > 1:
                del mapa[tirol-1][tiroc][mapa[tirol-1][tiroc].index('F')]
            if len(mapa[tirol][tiroc+1]) > 1:
                del mapa[tirol][tiroc+1][mapa[tirol][tiroc+1].index('F')]
            if len(mapa[tirol][tiroc-1]) > 1:
                del mapa[tirol][tiroc-1][mapa[tirol][tiroc-1].index('F')]
            break
def matrizX(mapa): 
    T = len(mapa) 
    matrizX = [] 
    for x in range(T): 
        linha = ["X"]*T 
        matrizX.append(linha) 
    matrizX[1][1] = "Y" 
    matrizX[1][0] = "P" 
    return matrizX 
mapa = dificuldade(input('Insira a dificuldade (easy, medium, hard): ').lower())
musica('dungeon')
limpa()
MatrizX = matrizX(mapa)
elegante(MatrizX)
dicionario = {}
dicionario['linha'] = 1 
dicionario['coluna'] = 1
MatrizX[dicionario['linha']][dicionario['coluna']] = "X"
dicionario['pontos'] = 0
tiro = 'não'
c = 0
print("Para se movimentar: \n W - para cima, A - para esquerda, D - para direita, S - para baixo \n")
print("Para atirar: \n U - para cima, H - para esquerda, K - para direita, J - para baixo \n")
while 1 < 2:
    key = getch().upper().decode('utf-8')
    c+=1
    if (key == "H" or key == "K" or key == "U" or key == "J") and (tiro != 0):
        shoot()
        linha = dicionario["linha"]
        coluna = dicionario["coluna"]
        while 1<2:
            c = 0
            MatrizX[dicionario['linha']][dicionario['coluna']] = mapa[dicionario['linha']][dicionario['coluna']]
            if ("R" not in MatrizX[linha][coluna]) and ("P" not in MatrizX[linha][coluna]):
                if "M" in mapa[linha][coluna]:
                    del mapa[linha][coluna][mapa[linha][coluna].index('M')]
                    print_h('Eu - isso é sangue!? para um brinquedo é bem realista \n Acertei em cheio ! ;)')
                    c +=1
                    break
                if key == "U":
                    linha -=1
                elif key == "K":
                    coluna+=1
                elif key == "H":
                    MatrizX[1][0] = "P"
                    coluna-= 1
                else:
                    linha+=1
                if linha > len(mapa)-1 or coluna > len(mapa)-1 or linha<0 or coluna <0:
                    break
                MatrizX[linha][coluna] = "Tiro"
                elegante(MatrizX)
                time.sleep(0.8)
                limpa()
                MatrizX[linha][coluna] = "X"
        if c == 0:
            print_h('Eu - parece que eu errei, deve ser só um cara fantasiado, não tem problema! #sad')
        tiro = 0 
    elif(key == "A" or key == "D" or key == "W" or key == "S"):
        mov = key
        limpa()
        movimento(mapa, dicionario['linha'], dicionario['coluna'], dicionario['pontos'])
        print_h(dicionario["frase"])
        print(" ")
        dicionario['pontos'] = dicionario['pontos'] - 1
        if dicionario["parar"] == "Break": 
            print("GAME ACABOU - PONTUAÇÃO = {}".format(dicionario['pontos']) + '\n' + "Mapa Completo --> ")
            elegante(mapa)
            input()
            break
        if dicionario['parar'] == 'ouro':
          pego = input().lower()
          if pego == 'sim':
            del mapa[dicionario["linha"]][dicionario["coluna"]][mapa[dicionario["linha"]][dicionario["coluna"]].index("@")]
            dicionario['pontos'] += 1000                                
    if c == 1:
        print(dicionario['pontos'])
        MatrizX[dicionario['linha']][dicionario['coluna']] = mapa[dicionario['linha']][dicionario['coluna']]
        elegante(MatrizX)
        MatrizX[dicionario['linha']][dicionario['coluna']] = "X"
        print("Para se movimentar: \n W - para cima, A - para esquerda, D - para direita, S - para baixo \n")
        if tiro !=0:
            print("Para atirar: \n U - para cima, H - para esquerda, K - para direita, J - para baixo \n")
    else:
        c = 0
print_h("Moça aleatória - Nossa, você conseguiu completar nosso brinquedo, qual seu nome? Talvez você entre no TOP 5,poucos conseguiram mesmo \n")
nome = input()
musica('fim')
limpa()
lista_pontos = []
lista_nome = []
lista_ordenada = []
if exists('score.txt') == False:
    score = open('score.txt', 'w')
    score.write(nome + ' | ' + str(dicionario['pontos']) + '\n')
    score.close()
    print('TOP FIVE \O/ \n' + nome + ' | ' + str(dicionario['pontos']))
else:
    score = open('score.txt', 'r')
    for n in score:
        lista_nome += [n.split(' | ')[0]]
        lista_pontos += [int(n.split(' | ')[1])]
        lista_ordenada += [int(n.split(' | ')[1])]
    while nome in lista_nome:
        nome = input('Você já jogou, assim não vale! \n Insira outro nome: \n')
        limpa()
    lista_nome += [nome]
    lista_pontos += [dicionario['pontos']]
    lista_ordenada += [dicionario['pontos']]
    lista_ordenada.sort()
    lista_ordenada.reverse()
    score.close()
    score = open('score.txt', 'a')
    score.write(nome + ' | ' + str(dicionario['pontos']) + '\n')
    score.close()
    print('TOP FIVE \O/')
    a = 0
    for valor in lista_ordenada:
        if a < 5:
            print(lista_nome[lista_pontos.index(valor)] + ' | ' + str(valor))
            indice = lista_pontos.index(valor)          
            del lista_pontos[indice]
            del lista_nome[indice]
            a += 1
        else:
            break
input()
