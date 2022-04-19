import pygame # Biblioteca que permite criação de jogos e executar arquivos de áudio

print("*"*10,"DESAFIO SOM","*"*10)

pygame.init()                           # 1
pygame.mixer.music.load('dorime.mp3')   # 2
pygame.mixer.music.play()               # 3
pygame.event.wait()                     # 4

# POR ORDEM:
# 1 - inicia a biblioteca
# 2 - carrega o arquivo de áudio
# 3 - executa o que foi carregado
# 4 - espera a execução