import pygame


pygame.init()

width = 960
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Life')

green = (0,255,0)
branco = (255,255,255)
preto = (0,0,0)
red = (255,0,0)
fonte = pygame.font.SysFont('',35)
msg = fonte.render('Aperte "ESPAÇO" para tirar vida', True, branco)
msgd = fonte.render('Aperte "ESPAÇO" para tirar vida', True, preto)
go = fonte.render('GUEIMI OUVER', True, branco)
tam = 400

rect4 = pygame.draw.rect(screen, green,(10,10,tam,15))

def telaInicial():
    rect4
    screen.blit(msg,(260,300))
    pygame.display.flip()

def dano(screen,rect4,tam):
    tamanho = tam - 10
    if tam == 10: 
        pygame.draw.rect(screen,(red),(10,10,tam,15))
        pygame.draw.rect(screen,(preto),(260,300,400,30))
        screen.blit(go,(400,300))
        return tam - 10
    else:
        pygame.draw.rect(screen, (255,0,0),(10,10,tam,15))
        pygame.draw.rect(screen, (green),(10,10,tamanho,15))
        return tamanho

telaInicial()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if not tam  < 10:
                if event.key == pygame.K_SPACE:
                    tam = dano(screen, rect4,tam)
        pygame.display.update()
                

