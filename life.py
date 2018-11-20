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
fonte_ = pygame.font.SysFont('',23)

lf_pc = fonte_.render('Your PC', True, branco)
lf_download = fonte_.render('DOWNLOADING...', True, branco)

msg = fonte.render('Aperte "ESPAÇO" para tirar vida', True, branco)
msg_ = fonte.render('Aperte "B" para Download', True, branco)
go = fonte.render('GUEIMI OUVER', True, branco)
yw = fonte.render('IU UIN', True, branco)

tam_download = 0
tam_pc = 300


#Definindo limite de vida através de linhas
pygame.draw.line(screen, branco, [11, 26], [11, 45], 1)
pygame.draw.line(screen, branco, [411, 26], [411, 45], 1)

pygame.draw.line(screen, branco, [11, 71], [11, 93], 1)
pygame.draw.line(screen, branco, [312, 71], [312, 93], 1)

#Barras de Vida
# rect_download = pygame.draw.rect(screen, preto,(12,28,tam_download,15))
rect_pc = pygame.draw.rect(screen, green,(12,74,tam_pc,15))


def telaInicial():
    screen.blit(lf_download, (10,10))
    screen.blit(lf_pc,(10,55))
    screen.blit(msg,(260,300))
    screen.blit(msg_,(260,350))
    pygame.display.flip()

def download(screen,tam):
    tamanho = tam + 10
    if tam == 390: 
        pygame.draw.rect(screen,green,(12,28,tamanho,15))
        pygame.draw.rect(screen,(preto),(260,300,400,30))
        pygame.draw.rect(screen,(preto),(260,350,400,30))
        screen.blit(yw,(400,300))
        return tam + 10
    else:
        pygame.draw.rect(screen, (green),(12,28,tamanho,15))
        return tamanho
    
def dano_pc(screen,tam):
    tamanho = tam - 10
    if tam == 10: 
        pygame.draw.rect(screen,(0,0,0),(12,74,tam,15))
        pygame.draw.rect(screen,(preto),(260,300,400,30))
        pygame.draw.rect(screen,(preto),(260,350,400,30))
        screen.blit(go,(400,300))
        return tam - 10
    else:
        pygame.draw.rect(screen, (0,0,0),(12,74,tam,15))
        pygame.draw.rect(screen, (green),(12,74,tamanho,15))
        return tamanho

telaInicial()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #Falta colocar função de parada caso derrota ou vitoria
            if not tam_pc  < 10 or not tam_download >290:
                if event.key == pygame.K_SPACE:
                    tam_pc = dano_pc(screen, tam_pc)
                if event.key == pygame.K_b:
                    tam_download = download(screen, tam_download)
                    
        pygame.display.update()
                

