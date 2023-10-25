import random
from time import sleep

palavraChave = ['santacruz', 'sport', 'retro', 'salgueiro', 'ibis', 'caruarucity', 'nautico']
letraUsuario = []
chances = 6
ganhou = False
emojiDemonio = '😈'
print('Olá caro jogador, seja bem vindo(a) ao jogo da forca com alguns times de pernambuco!! ')
sleep(3)
nome = input('Vamos começar?! Primeiro, informe seu nome: ')
sleep(1)
print(f'Olá {nome}, Bem vindo(a), fique atento as informações!!')
sleep(2)
print('Acerte a palavra chave e ganhe o game!!')
sleep(3)
print('Serão 6 tentativas, cada erro uma tentativa a menos!')
sleep(3)
print('Após as 6 tentativas ERRADAS você estará...')
sleep(4)
print(f'MORTOO...{emojiDemonio}!!!')
sleep(2)
print('Ok,Vamos começar?!')
sleep(1)
print('Carregando a palavra...')
sleep(3)

def escolherPalavra(palavraChave):
    return random.choice(palavraChave)


palavraEscolhida = escolherPalavra(palavraChave)

forca = [
    '''
               --------
               |      |
               |
               |
               |
               |
            ====
    ''',
    '''
       --------
       |      |
       |      O
       |
       |
       |
    ====
    ''',
    '''
       --------
       |      |
       |      O
       |      |
       |
       |
    ====
    ''',
    '''
       --------
       |      |
       |      O
       |     /|
       |
       |
    ====
    ''',
    '''
       --------
       |      |
       |      O
       |     /|\ 
       |
       |
    ====  
    '''
    ,
    '''
       --------
       |      |
       |      O
       |     /|\ 
       |     /
       |
    ====
    ''',
    '''
       --------
       |      |
       |      O
       |     /|\ 
       |     / \ 
       |
    ==== 
    '''
]

while True:
    palavraExibida = ''
    for letra in palavraEscolhida:
        if letra.lower() in letraUsuario:
            palavraExibida += letra + ' '
        else:
            palavraExibida += '_ '
    print(palavraExibida)

    if all(letra in letraUsuario for letra in palavraEscolhida):
        ganhou = True
        break

    tentativa = input('Informe uma letra: ').lower()
    letraUsuario.append(tentativa)

    if tentativa not in palavraEscolhida:
        chances -= 1

    if chances == 0:
        break

    if tentativa not in palavraEscolhida:
        print(f'Letra "{tentativa}" não está na palavra-chave.')
        print('Forca:')
        print(forca[6 - chances])

if ganhou:
    print(f'Parabéns, você ganhou! A palavra era {palavraEscolhida}')
else:
    print(f'Você perdeu! A palavra era {palavraEscolhida}')
