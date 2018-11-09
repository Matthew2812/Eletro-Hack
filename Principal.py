import pygame, sys, os, Funcoes

pygame.init()
pygame.font.init()

width = 960
height = 600
tela = pygame.image.load(os.path.join("C:/Users/Matheus/Documents/Jogo/Imagens","Tela Principal.jpg"))

screen = pygame.display.set_mode((width, height))

branco = (255,255,255)
vermelho = (255,0,0)
verde = (55,255,35)
preto = (0,0,0)
font = pygame.font.SysFont("HACKED Regular.ttf",35)
text_play = font.render("JOGAR",True, branco)
text_instrucoes = font.render("INSTRUÇOES", True, branco)
text_creditos = font.render("CREDITOS", True, branco)



cor_rect = preto
rect_um = False
rect_dois = False
rect_tres = False


screen.blit(tela,(0,0))
screen.blit(text_play,(421,393))
screen.blit(text_instrucoes,(383,462))
screen.blit(text_creditos,(400, 532))


pygame.display.flip()

running = True
while running:
    rect4 = pygame.draw.rect(screen, branco,(379,374,170,60),3)
    rect5 = pygame.draw.rect(screen, branco,(379,444,170,60),3)
    rect6 = pygame.draw.rect(screen, branco,(379,514,170,60),3)
    if rect_um:
        rect1 = pygame.draw.rect(screen, cor_rect,(381,375,166,58))
        screen.blit(text_play,(421,393))
    elif rect_dois:
        rect2 = pygame.draw.rect(screen, cor_rect,(381,445,166,58))
        screen.blit(text_instrucoes,(383,462))
    elif rect_tres:
        rect3 = pygame.draw.rect(screen, cor_rect,(381,515,166,58))
        screen.blit(text_creditos,(400, 532))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if (380< mouse_x <550) and(375< mouse_y <435):
        cor_rect = verde
        rect_um = True
        rect_dois = False
        rect_tres = False
    elif (380< mouse_x <550) and(445< mouse_y <505):
        cor_rect = verde
        rect_dois = True
        rect_um = False
        rect_tres = False
    elif (380< mouse_x <550) and(515< mouse_y <575):
        cor_rect = verde
        rect_tres = True
        rect_um = False
        rect_dois = False
    else:
        cor_rect = preto
   
    pygame.display.flip()
        
pygame.quit()
sys.exit()
    
