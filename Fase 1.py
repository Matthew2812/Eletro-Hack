import pygame,sys,os,time

pygame.init()
pygame.mixer.init()

def ritmoAmarelo(cont, linha, sinal, espaco):
    if cont < 1.9:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(125,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(720,0))
    elif cont < 2.3:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(325,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(720,0))
    elif cont < 2.7:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(525,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(720,0))
    elif cont < 3.2:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(725,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(720,0))
    elif cont < 5.6:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
    elif cont < 6.2:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(125,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(720,0))
    elif cont < 6.5:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(325,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(720,0))
    elif cont < 7.3:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(525,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(720,0))
    elif cont < 7.8:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(725,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(720,0))
    else:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))

def ritmoAmareloInvertido(cont, linha, sinal, espaco):
    if cont < 1.9:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(725,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(700,0))
    elif cont < 2.3:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(525,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
    elif cont < 2.7:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(325,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(700,0))
    elif cont < 3.2:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(125,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(700,0))
    elif cont < 5.6:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
    elif cont < 6.2:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(725,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(700,0))
    elif cont < 6.5:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(525,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(700,0))
    elif cont < 7.3:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(325,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(700,0))
    elif cont < 7.8:
        if not espaco:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(sinal,(125,257))
        else:
            screen.fill((0,0,0))
            screen.blit(linha,(100,300))
            screen.blit(barra,(700,0))
    else:
        screen.fill((0,0,0))
        screen.blit(linha,(100,300))
        cont_amarelo = 1

def ritmoVermelho(cont, linha, sinal, espaco):
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

def ritmoVermelhoDois(cont, linha, sinal, espaco):
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
        ritmoAmarelo(tempo, linha_amarela, sinal_amarelo, espaco)
    elif tempo < 19.4:
        ritmoAmarelo(tempo-9.6, linha_amarela, sinal_amarelo, espaco)
    elif tempo < 29:
        ritmoAmareloInvertido(tempo-19.2, linha_amarela, sinal_amarelo, espaco)
    elif tempo < 38.5:
        ritmoAmareloInvertido(tempo-28.8, linha_amarela, sinal_amarelo, espaco)
    elif tempo < 39.8:
        ritmoVermelho(tempo-38.5, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 41:
        ritmoVermelhoDois(tempo-39.8, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 42.2:
        ritmoVermelho(tempo-41, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 43.4:
        ritmoVermelhoDois(tempo-42.2, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 44.6:
        ritmoVermelho(tempo-43.4, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 45.8:
        ritmoVermelhoDois(tempo-44.6, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 47:
        ritmoVermelho(tempo-45.8, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 48.2:
        ritmoVermelhoDois(tempo-47, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 49.4:
        ritmoVermelho(tempo-48.2, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 50.6:
        ritmoVermelhoDois(tempo-49.4, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 51.8:
        ritmoVermelho(tempo-50.6, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 53:
        ritmoVermelhoDois(tempo-51.8, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 54.2:
        ritmoVermelho(tempo-53, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 55.4:
        ritmoVermelhoDois(tempo-54.2, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 56.6:
        ritmoVermelho(tempo-55.4, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 57.8:
        ritmoVermelhoDois(tempo-56.6, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 77:
        screen.fill((0,0,0))
        screen.blit(linha_vermelha,(100,100))
        screen.blit(linha_vermelha,(100,500))
    elif tempo < 78.2:
        ritmoVermelho(tempo-77, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 79.4:
        ritmoVermelhoDois(tempo-78.2, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 80.6:
        ritmoVermelho(tempo-79.4, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 81.8:
        ritmoVermelhoDois(tempo-80.6, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 83:
        ritmoVermelho(tempo-81.8, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 84.2:
        ritmoVermelhoDois(tempo-83, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 85.4:
        ritmoVermelho(tempo-84.2, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 86.6:
        ritmoVermelhoDois(tempo-85.4, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 87.8:
        ritmoVermelho(tempo-86.6, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 89:
        ritmoVermelhoDois(tempo-87.8, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 90.2:
        ritmoVermelho(tempo-89, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 91.4:
        ritmoVermelhoDois(tempo-90.2, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 92.6:
        ritmoVermelho(tempo-91.4, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 93.8:
        ritmoVermelhoDois(tempo-92.6, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 95:
        ritmoVermelho(tempo-93.8, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 96.2:
        ritmoVermelhoDois(tempo-95, linha_vermelha, sinal_vermelho, espaco)
    elif tempo < 106:
        ritmoAmareloInvertido(tempo-96, linha_amarela, sinal_amarelo, espaco)
    elif tempo < 115.6:
        ritmoAmareloInvertido(tempo-105.6, linha_amarela, sinal_amarelo, espaco)
    elif tempo < 125.2:
        ritmoAmarelo(tempo-115.2, linha_amarela, sinal_amarelo, espaco)
    elif tempo < 134.8:
        ritmoAmarelo(tempo-124.8, linha_amarela, sinal_amarelo, espaco)
        
width = 960
height = 600

screen = pygame.display.set_mode((width, height))

linha_amarela = pygame.image.load(os.path.join("Imagens","Linha Amarela.jpg"))
sinal_amarelo = pygame.image.load(os.path.join("Imagens","Sinal Amarelo.jpg"))
linha_vermelha = pygame.image.load(os.path.join("Imagens","Linha Vermelha.jpg"))
sinal_vermelho = pygame.image.load(os.path.join("Imagens","Sinal Vermelho.jpg"))
chill_wave = pygame.mixer.music.load(os.path.join("Musica","Chill Wave.mp3"))
barra = pygame.image.load(os.path.join("Imagens","Espaco.jpg"))
espaco = False
pont = 0
verificador = False

barra.set_alpha(100)

pygame.mixer.music.play()

cont_amarelo = 0

screen.fill((0,0,0))

running = True
while running:
    tempo = time.clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                espaco = True
                verificador = True
        '''

    print(tempo, espaco, verificador, pont)
    tempoJogo(tempo)

    '''
    if 3.2 < tempo < 5.6 and espaco:
        espaco = False
    elif 7.8 < tempo < 9.8 and espaco:
        espaco = False
    elif 13 < tempo < 15.4 and espaco:
        espaco = False
    elif 17.6 < tempo < 19.8 and espaco:
        espaco = False


        
    if 2.7 < tempo < 3.2 and espaco and verificador:
        pont += 1
        verificador = False
    elif 7.3 < tempo < 7.8 and espaco and verificador:
        pont += 1
        verificador = False
    elif 12.3 < tempo < 12.8 and espaco and verificador:
        pont += 1
        verificador = False
    elif 16.9 < tempo < 17.4 and espaco and verificador:
        pont += 1
        verificador = False
        
    if tempo < 2.7 and verificador:
        verificador = False
    elif tempo < 7.3 and verificador:
        verificador = False
    elif tempo < 12.5 and verificador:
        verificador = False
    elif tempo < 17.1 and verificador:
        verificador = False
    '''
    
    pygame.display.flip()
    

pygame.quit()
sys.exit()
