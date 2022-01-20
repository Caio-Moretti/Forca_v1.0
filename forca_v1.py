# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (Tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.correct_letters = []

    # Método que pega o chute da letra, verifica se está na palavra e joga a letra pra uma das listas
    def guess(self, letter):
        if letter in self.word and letter not in self.correct_letters:
            self.correct_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or len(self.missed_letters) == 6

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' in self.hide_word():
            return False
        return True

    # Método para não mostrar a letra no board
    def hide_word(self):
        rtn = ''
        for l in self.word:
            if l not in self.correct_letters:
                rtn += '_'
            else:
                rtn += l
        return rtn

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print(f'\nPalavra: {self.hide_word()}')
        print(f'\nLetras Erradas: ',)
        for l in self.missed_letters:
            print(l,)
        print()
        print(f'\nLetas Corretas: ',)
        for l in self.correct_letters:
            print(l,)
        print()


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():

    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        game.guess(str(input('\nDigite uma letra: ')))

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
