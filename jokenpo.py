from  random import choice
def função_espaço():
    print()
def jokenpo():
    resposta = ''
    while True:
        jogador = str(input('Você que pedra, papel ou tesoura?: ')).lower() 
        maquina = choice(['pedra', 'papel', 'tesoura'])
        função_espaço()
        print(f'A máquina escolheu: {maquina}')
        função_espaço()  
        if jogador == maquina:
            print('\033[1;33m EMPATE \033[0;0m')
        
        elif ganhar_jogo(jogador, maquina):
            print('\033[1;32m VOCÊ GANHOU! \033[0;0m')
            

        else:
            print('\033[1;31m VOCÊ PERDEU! \033[0;0m')
            
        
        resposta = str(input('Deseja continuar? [S|N]')).lower()
        if resposta not in 'SsNn':
            print('Digite apena S ou N para sua resposta')
        elif resposta in 'Nn':
            break
    print(f'Ok, até outra hora!')
        


def ganhar_jogo(jogador, maquina):
    if jogador in 'pedra' and maquina in 'tesoura':
        return True
    elif jogador in 'papel' and maquina in 'pedra':
        return True
    elif jogador in 'tesoura' and maquina in 'papel':
        return True



jokenpo()



