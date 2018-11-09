import pygame,sys,os,time

pygame.init()
pygame.mixer.init()

def ritmoAmarelo(cont, linha, sinal):
    if cont < 1.9:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(125,257))
    elif cont < 2.3:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(325,257))
    elif cont < 2.7:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(525,257))
    elif cont < 3.2:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(725,257))
    elif cont < 5.6:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
    elif cont < 6.2:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(125,257))
    elif cont < 6.5:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(325,257))
    elif cont < 7.3:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(525,257))
    elif cont < 7.8:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(725,257))
    else:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))

def ritmoAmareloInvertido(cont, linha, sinal):
    if cont < 1.9:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(725,257))
    elif cont < 2.3:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(525,257))
    elif cont < 2.7:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(325,257))
    elif cont < 3.2:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(125,257))
    elif cont < 5.6:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
    elif cont < 6.2:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(725,257))
    elif cont < 6.5:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(525,257))
    elif cont < 7.3:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(325,257))
    elif cont < 7.8:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(125,257))
    else:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        cont_amarelo = 1

def ritmoVermelho(cont, linha, sinal):
    if cont < 0.7:
        screen.fill((0,0,0))
        screen.blit(linha,(100,100))
        screen.blit(linha,(100,500))
        screen.blit(sinal,(125,57))
    elif cont < 1.3:
        screen.fill((0,0,0))
        screen.blit(linha,(100,100))
        screen.blit(linha,(100,500))
        screen.blit(sinal,(725,57))

def ritmoVermelhoDois(cont, linha, sinal):
    if cont < 0.7:
        screen.fill((0,0,0))
        screen.blit(linha,(100,500))
        screen.blit(linha,(100,100))
        screen.blit(sinal,(125,457))
    elif cont < 1.3:
        screen.fill((0,0,0))
        screen.blit(linha,(100,500))
        screen.blit(linha,(100,100))
        screen.blit(sinal,(725,457))

def tempoJogo(tempo):
    if tempo < 9.8:
        ritmoAmarelo(tempo, linha_amarela, sinal_amarelo)
    elif tempo < 19.4:
        ritmoAmarelo(tempo-9.6, linha_amarela, sinal_amarelo)
    elif tempo < 29:
        ritmoAmareloInvertido(tempo-19.2, linha_amarela, sinal_amarelo)
    elif tempo < 38.5:
        ritmoAmareloInvertido(tempo-28.8, linha_amarela, sinal_amarelo)
    elif tempo < 39.8:
        ritmoVermelho(tempo-38.5, linha_vermelha, sinal_vermelho)
    elif tempo < 41:
        ritmoVermelhoDois(tempo-39.8, linha_vermelha, sinal_vermelho)
    elif tempo < 42.2:
        ritmoVermelho(tempo-41, linha_vermelha, sinal_vermelho)
    elif tempo < 43.4:
        ritmoVermelhoDois(tempo-42.2, linha_vermelha, sinal_vermelho)
    elif tempo < 44.6:
        ritmoVermelho(tempo-43.4, linha_vermelha, sinal_vermelho)
    elif tempo < 45.8:
        ritmoVermelhoDois(tempo-44.6, linha_vermelha, sinal_vermelho)
    elif tempo < 47:
        ritmoVermelho(tempo-45.8, linha_vermelha, sinal_vermelho)
    elif tempo < 48.2:
        ritmoVermelhoDois(tempo-47, linha_vermelha, sinal_vermelho)
    elif tempo < 49.4:
        ritmoVermelho(tempo-48.2, linha_vermelha, sinal_vermelho)
    elif tempo < 50.6:
        ritmoVermelhoDois(tempo-49.4, linha_vermelha, sinal_vermelho)
    elif tempo < 51.8:
        ritmoVermelho(tempo-50.6, linha_vermelha, sinal_vermelho)
    elif tempo < 53:
        ritmoVermelhoDois(tempo-51.8, linha_vermelha, sinal_vermelho)
    elif tempo < 54.2:
        ritmoVermelho(tempo-53, linha_vermelha, sinal_vermelho)
    elif tempo < 55.4:
        ritmoVermelhoDois(tempo-54.2, linha_vermelha, sinal_vermelho)
    elif tempo < 56.6:
        ritmoVermelho(tempo-55.4, linha_vermelha, sinal_vermelho)
    elif tempo < 57.8:
        ritmoVermelhoDois(tempo-56.6, linha_vermelha, sinal_vermelho)
    elif tempo < 77:
        screen.fill((0,0,0))
        screen.blit(linha_vermelha,(100,100))
        screen.blit(linha_vermelha,(100,500))
    elif tempo < 78.2:
        ritmoVermelho(tempo-77, linha_vermelha, sinal_vermelho)
    elif tempo < 79.4:
        ritmoVermelhoDois(tempo-78.2, linha_vermelha, sinal_vermelho)
    elif tempo < 80.6:
        ritmoVermelho(tempo-79.4, linha_vermelha, sinal_vermelho)
    elif tempo < 81.8:
        ritmoVermelhoDois(tempo-80.6, linha_vermelha, sinal_vermelho)
    elif tempo < 83:
        ritmoVermelho(tempo-81.8, linha_vermelha, sinal_vermelho)
    elif tempo < 84.2:
        ritmoVermelhoDois(tempo-83, linha_vermelha, sinal_vermelho)
    elif tempo < 85.4:
        ritmoVermelho(tempo-84.2, linha_vermelha, sinal_vermelho)
    elif tempo < 86.6:
        ritmoVermelhoDois(tempo-85.4, linha_vermelha, sinal_vermelho)
    elif tempo < 87.8:
        ritmoVermelho(tempo-86.6, linha_vermelha, sinal_vermelho)
    elif tempo < 89:
        ritmoVermelhoDois(tempo-87.8, linha_vermelha, sinal_vermelho)
    elif tempo < 90.2:
        ritmoVermelho(tempo-89, linha_vermelha, sinal_vermelho)
    elif tempo < 91.4:
        ritmoVermelhoDois(tempo-90.2, linha_vermelha, sinal_vermelho)
    elif tempo < 92.6:
        ritmoVermelho(tempo-91.4, linha_vermelha, sinal_vermelho)
    elif tempo < 93.8:
        ritmoVermelhoDois(tempo-92.6, linha_vermelha, sinal_vermelho)
    elif tempo < 95:
        ritmoVermelho(tempo-93.8, linha_vermelha, sinal_vermelho)
    elif tempo < 96.2:
        ritmoVermelhoDois(tempo-95, linha_vermelha, sinal_vermelho)
    elif tempo < 106:
        ritmoAmareloInvertido(tempo-96, linha_amarela, sinal_amarelo)
    elif tempo < 115.6:
        ritmoAmareloInvertido(tempo-105.6, linha_amarela, sinal_amarelo)
    elif tempo < 125.2:
        ritmoAmarelo(tempo-115.2, linha_amarela, sinal_amarelo)
    elif tempo < 134.8:
        ritmoAmarelo(tempo-124.8, linha_amarela, sinal_amarelo)
        
width = 960
height = 600

screen = pygame.display.set_mode((width, height))

linha_amarela = pygame.image.load(os.path.join("Imagens","Linha Amarela.jpg"))
sinal_amarelo = pygame.image.load(os.path.join("Imagens","Sinal Amarelo.jpg"))
linha_vermelha = pygame.image.load(os.path.join("Imagens","Linha Vermelha.jpg"))
sinal_vermelho = pygame.image.load(os.path.join("Imagens","Sinal Vermelho.jpg"))
chill_wave = pygame.mixer.music.load(os.path.join("Musica","Chill Wave.mp3"))


pygame.mixer.music.play()

cont_amarelo = 0

screen.fill((0,0,0))

running = True
while running:
    tempo = time.clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tempoJogo(tempo)
    

        

    pygame.display.flip()
    

pygame.quit()
sys.exit()
