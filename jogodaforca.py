import os
class JogodaForca:
    def __init__(self, palavra_secreta):
        self.palavra_secreta = palavra_secreta
        self.lista_de_acertos = ['_' for _ in palavra_secreta]
        self.tentativas = 6
        self.letras_tentadas = []
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def exibir_estado_atual(self):
        print(''.join(self.lista_de_acertos))
        print(f'Tentativas restantes: {self.tentativas}')
        print(f'Letras tentadas: {self.letras_tentadas}')
    def verificar_letra(self,letra):
        if letra in self.letras_tentadas:
            print('Você já tentou essa letra!')
        else:
            self.letras_tentadas.append(letra)
            if letra in self.palavra_secreta:
                for indice, caractere in enumerate(self.palavra_secreta):
                    if caractere == letra:
                        self.lista_de_acertos[indice] = letra
                    else:
                        self.tentativas -= 1
    def palavra_descoberta(self):
        return '_' not in self.lista_de_acertos
    def iniciar_jogo(self):
        while self.tentativas > 0 and not self.palavra_descoberta():
            self.exibir_estado_atual()
            letra_do_jogasdor = input('Digite uma letra: ').lower().strip()
            if len(letra_do_jogasdor) == 1:
                self.verificar_letra(letra_do_jogasdor)
            else:
                print('Por favor, digite apenas uma letra.')
        if self.palavra_descoberta:
            print(f'Parabéns, você ganhou! A palavra era: {self.palavra_secreta}')
        else:
            print(f'Fim de jogo! A palavra era: {self.palavra_secreta}')
def main():
    print('Bem Vindo ao Jogo da Forca!')
    palavra_secreta = input('Digite a palavra secreta: ').lower().strip()
    jogo = JogodaForca(palavra_secreta)
    jogo.limpar_tela()
    jogo.iniciar_jogo()
if __name__ == '__main__':
    main()