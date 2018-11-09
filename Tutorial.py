import pygame,sys,os,time

pygame.mixer.init()
pygame.init()

def ritmoVerde(cont, linha, sinal):
    if cont < 1.5:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(125,257))
    elif cont < 3:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(225,257))
    elif cont < 4.5:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(325,257))
    elif cont < 6:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(425,257))
    elif cont < 7.5:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(525,257))
    elif cont < 9:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(625,257))
    elif cont < 10.5:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(725,257))
    elif cont < 12:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        

def ritmoAmarelo(cont, linha, sinal):
    if cont < 1.5:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(125,257))
    elif cont < 3:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(325,257))
    elif cont < 4.5:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(525,257))
    elif cont < 6:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(725,257))
    elif cont < 7.5:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))

def ritmoVermelho(cont, linha, sinal):
    if cont < 1.5:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(125,257))
    elif cont < 3:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        screen.blit(sinal,(725,257))
    elif cont < 4.5:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))

def som():
    if 1.900 < tempo < 1.906:
        kick.stop()
        kick.play()
    elif 3.400 < tempo < 3.406:
        kick.stop()
        kick.play()
    elif 4.900 < tempo < 4.906:
        kick.stop()
        kick.play()
    elif 6.400 < tempo < 6.406:
        kick.stop()
        kick.play()
    elif 7.900 < tempo < 7.906:
        kick.stop()
        kick.play()
    elif 9.400 < tempo < 9.406:
        kick.stop()
        kick.play()
    elif 10.900 < tempo < 10.906:
        clap.stop()
        clap.play()

    elif 12.900 < tempo < 12.906:
        kick.stop()
        kick.play()
    elif 14.400 < tempo < 14.406:
        kick.stop()
        kick.play()
    elif 15.900 < tempo < 15.906:
        kick.stop()
        kick.play()
    elif 17.400 < tempo < 17.406:
        clap.stop()
        clap.play()

    elif  19.900 < tempo < 19.906:
        kick.stop()
        kick.play()
    elif 21.400 < tempo < 21.406:
        clap.stop()
        clap.play()
        
width = 960
height = 600

screen = pygame.display.set_mode((width, height))

linha_amarela = pygame.image.load(os.path.join("Imagens","Linha Amarela.jpg"))
sinal_amarelo = pygame.image.load(os.path.join("Imagens","Sinal Amarelo.jpg"))
linha_vermelha = pygame.image.load(os.path.join("Imagens","Linha Vermelha.jpg"))
sinal_vermelho = pygame.image.load(os.path.join("Imagens","Sinal Vermelho.jpg"))
linha_verde = pygame.image.load(os.path.join("Imagens","Linha Verde.jpg"))

sinal_verde = pygame.image.load(os.path.join("Imagens","Sinal Verde.jpg"))
kick = pygame.mixer.Sound("Kick.wav")
clap = pygame.mixer.Sound("Clap.wav")

kick.set_volume(1)
cont_amarelo = 0

screen.fill((0,0,0))

running = True
while running:
    tempo = pygame.time.get_ticks()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    som()
    if 2 < tempo < 13:
        ritmoVerde(tempo-2, linha_verde, sinal_verde)
    elif 13 < tempo < 20:
        ritmoAmarelo(tempo-13, linha_amarela, sinal_amarelo)
    elif 20 < tempo < 26:
        ritmoVermelho(tempo-20, linha_vermelha, sinal_vermelho)
    

        

    pygame.display.flip()
    

pygame.quit()
sys.exit()
