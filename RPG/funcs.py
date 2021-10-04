from classes import *
import os

listMago = []
listCavaleiro = []
listArqueiro = []

def clearScreen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# MENUS

def printMenuTestes():
    print('----- TESTES -----')
    print('- 1. MAGO        -')
    print('- 2. CAVALEIRO   -')
    print('- 3. ARQUEIRO    -')
    print('- 4. SAIR        -')
    print('------------------')
    return int(input('Entrada: '))

def menuTestes():
    vENTRADA = 0
    while(vENTRADA != 4):
        vENTRADA = printMenuTestes()
        if(vENTRADA == 1):
            clearScreen()
            menuMagos()
            pass
        elif(vENTRADA == 2):
            clearScreen()
            menuCavaleiros()
        elif(vENTRADA == 3):
            clearScreen()
            menuArqueiros()
        elif(vENTRADA == 4):
            clearScreen()
            print('-----'*10)
            print('OBRIGADO POR JOGAR!'.center(50, ' '))
            print('LUCAS MELLO DOS SANTOS - 21410436'.center(50, ' '))
            print('-----'*10)
            break

def menuMagos():
    vENTRADA = 0
    while(vENTRADA != 4):
        vENTRADA = menuMago()
        if(vENTRADA == 1):
            addMago()
        elif(vENTRADA == 2):
            clearScreen()
            listarMagos()
            pass
        elif(vENTRADA == 3):
            clearScreen()
            ataqueMago()
            pass
        elif(vENTRADA == 4):
            clearScreen()
            break

def menuCavaleiros():
    vENTRADA = 0
    while(vENTRADA != 4):
        vENTRADA = menuCavaleiro()
        if(vENTRADA == 1):
            addCavaleiro()
        elif(vENTRADA == 2):
            clearScreen()
            listarCavaleiros()
            pass
        elif(vENTRADA == 3):
            clearScreen()
            ataqueCavaleiro()
            pass
        elif(vENTRADA == 4):
            clearScreen()
            break

def menuArqueiros():
    vENTRADA = 0
    while(vENTRADA != 4):
        vENTRADA = menuArqueiro()
        if(vENTRADA == 1):
            addArqueiro()
        elif(vENTRADA == 2):
            clearScreen()
            listarArqueiros()
            pass
        elif(vENTRADA == 3):
            clearScreen()
            ataqueArqueiro()
            pass
        elif(vENTRADA == 4):
            clearScreen()
            break

def menuMago():
    print('------ MAGO ------')
    print('- 1. ADD MAGO    -')
    print('- 2. VER MAGOS   -')
    print('- 3. ATAQUE      -')
    print('- 4. SAIR        -')
    print('------------------')
    vENTRADA = int(input('Entrada: '))
    return vENTRADA

def menuCavaleiro():
    print('------ CAVALEIRO ------')
    print('- 1. ADD CAVALEIRO    -')
    print('- 2. VER CAVALEIROS   -')
    print('- 3. ATAQUE           -')
    print('- 4. SAIR             -')
    print('-----------------------')
    vENTRADA = int(input('Entrada: '))
    return vENTRADA

def menuArqueiro():
    print('------ ARQUEIRO ------')
    print('- 1. ADD ARQUEIRO    -')
    print('- 2. VER ARQUEIROS   -')
    print('- 3. ATAQUE          -')
    print('- 4. SAIR            -')
    print('----------------------')
    vENTRADA = int(input('Entrada: '))
    return vENTRADA

# CAVALEIRO

def addCavaleiro():
    print('----- ADD CAVALEIRO ----')
    nome = input('NOME: ')
    HP = int(input('Health Points (HP): '))
    SP = int(input('Strength Power (SP): '))
    print('------------------------')
    clearScreen()
    
    CAVALEIRO = Cavaleiro(nome, HP, SP)
    listCavaleiro.append(CAVALEIRO)
    
def listarCavaleiros():
    for cavaleiro in listCavaleiro:
        cavaleiro.getInfos()

def searchCavaleiroAD(nome):
    for cavaleiro in listCavaleiro:
        if cavaleiro.getNome() == nome:
            return cavaleiro.getAD()

def ataqueCavaleiro():
    print('Deseja atacar com qual cavaleiro? ')
    listarCavaleiros()
    nome = input('Entrada: ')
    print('{} atacou o dummy causando {} pontos de dano físico!'.format(nome, searchCavaleiroAD(nome)))

# ARQUEIRO

def addArqueiro():
    print('----- ADD ARQUEIRO ----')
    nome = input('NOME: ')
    HP = int(input('Health Points (HP): '))
    SP = int(input('Strength Power (SP): '))
    print('------------------------')
    clearScreen()
    
    ARQUEIRO = Arqueiro(nome, HP, SP)
    listArqueiro.append(ARQUEIRO)
    
def listarArqueiros():
    for arqueiro in listArqueiro:
        arqueiro.getInfos()

def searchArqueiroRP(nome):
    for arqueiro in listArqueiro:
        if arqueiro.getNome() == nome:
            return arqueiro.getRP()

def ataqueArqueiro():
    print('Deseja atacar com qual arqueiro? ')
    listarArqueiros()
    nome = input('Entrada: ')
    print('{} atacou o dummy causando {} pontos de dano a distancia!'.format(nome, searchArqueiroRP(nome)))

# MAGO

def addMago():
    print('----- ADD MAGO ----')
    nome = input('NOME: ')
    HP = int(input('Health Points (HP): '))
    SP = int(input('Strength Power (SP): '))
    print('-------------------')
    clearScreen()
    
    MAGO = Mago(nome, HP, SP)
    listMago.append(MAGO)
    
def listarMagos():
    for magos in listMago:
        magos.getInfos()

def searchMagoMP(nome):
    for mago in listMago:
        if mago.getNome() == nome:
            return mago.getMP()

def ataqueMago():
    print('Deseja atacar com qual mago? ')
    listarMagos()
    nome = input('Entrada: ')
    print('{} atacou o dummy causando {} pontos de dano mágico!'.format(nome, searchMagoMP(nome)))