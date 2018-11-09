import pygame,sys,os


#Iniciando Pygame e Fontes
pygame.init()
pygame.font.init()

#Largura e Altura da tela
width = 960
height = 600

#Telas do menu
tela_inicial = pygame.image.load(os.path.join("C:/Users/Matheus/Documents/Jogo/Imagens","Tela Principal.jpg"))
tela_musicas = pygame.image.load(os.path.join("C:/Users/Matheus/Documents/Jogo/Imagens","Tela Musicas.jpg"))
tela_creditos = pygame.image.load(os.path.join("C:/Users/Matheus/Documents/Jogo/Imagens","Tela Creditos.jpg"))
tela_instrucoes = pygame.image.load(os.path.join("C:/Users/Matheus/Documents/Jogo/Imagens","Tela Instrucoes.jpg"))

#Variáveis pra confirmar cada tela (tela1 = tela inicial, tela2 = tela do jogo estática, tela3 = tela de créditos, tela4 = tela de instruções)
tela1 = True
tela2 = False
tela3 = False
tela4 = False

#Criando a tela
screen = pygame.display.set_mode((width, height))

#Cores
branco = (255,255,255)
vermelho = (255,0,0)
verde = (55,255,35)
preto = (0,0,0)

#Fonte e textos
font = pygame.font.SysFont("HACKED Regular.ttf",35)
text_play = font.render("JOGAR",True, branco)
text_instrucoes = font.render("INSTRUÇOES", True, branco)
text_creditos = font.render("CREDITOS", True, branco)
text_voltar = font.render("VOLTAR",True,branco)


#Cor do retangulo e váriaveis pra salvar a cor dele (Efeito pra mudar quando mouse em cima do botão)
cor_rect = preto
rect_inicial_um = False
rect_inicial_dois = False
rect_inicial_tres = False
rect_creditos = False
rect_instrucoes = False
rect_jogar = False

#Função pra criar a tela Inicial
def telaInicial():
    screen.blit(tela_inicial,(0,0))
    screen.blit(text_play,(421,393))
    screen.blit(text_instrucoes,(383,462))
    screen.blit(text_creditos,(400, 532))
    rect4 = pygame.draw.rect(screen, branco,(379,374,170,60),3)
    rect5 = pygame.draw.rect(screen, branco,(379,444,170,60),3)
    rect6 = pygame.draw.rect(screen, branco,(379,514,170,60),3)

telaInicial()

    
pygame.display.flip()

#Loop infinito
running = True
while running:
    #Pegando o movimento e o click do mouse. Mudando as telas
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and rect_inicial_um and tela1:
            tela2 = True
            tela1 = False
            tela3 = False
            tela4 = False
        if event.type == pygame.MOUSEBUTTONDOWN and rect_inicial_tres and tela1:
            tela2 = False
            tela1 = False
            tela3 = True
            tela4 = False
        if event.type == pygame.MOUSEBUTTONDOWN and rect_inicial_dois and tela1:
            tela4 = True
            tela1 = False
            tela2 = False
            tela3 = False
        if event.type == pygame.MOUSEBUTTONDOWN and rect_jogar and tela2:
            tela1 = True
            tela2 = False
            tela3 = False
            tela4 = False
            telaInicial()
        if event.type == pygame.MOUSEBUTTONDOWN and rect_instrucoes and tela4:
            tela1 = True
            tela2 = False
            tela3 = False
            tela4 = False
            telaInicial()
        if event.type == pygame.MOUSEBUTTONDOWN and rect_creditos and tela3:
            tela2 = False
            tela1 = True
            tela3 = False
            tela4 = False
            telaInicial()
            
    #Verificando qual tela está no momento
    if tela2:
        screen.blit(tela_musicas,(0,0))
        rect12 = pygame.draw.rect(screen, branco,(750,500,170,60),3)
        screen.blit(text_voltar,(789,519))
        tela1 = False
        tela3 = False
        tela4 = False
    if tela3:
        screen.blit(tela_creditos,(0,0))
        rect8 = pygame.draw.rect(screen, branco,(750,500,170,60),3)
        screen.blit(text_voltar,(789, 519))
        tela1 = False
        tela2 = False
        tela4 = False
    if tela4:
        screen.blit(tela_instrucoes,(0,0))
        rect10 = pygame.draw.rect(screen, branco,(750,500,170,60),3)
        screen.blit(text_voltar,(789, 519))
        tela1 = False
        tela3 = False
        tela2 = False
    
    #Verificando a cor dos retangulos pro efeito
    if rect_inicial_um and tela1:
        rect1 = pygame.draw.rect(screen, cor_rect,(381,375,166,58))
        screen.blit(text_play,(421,393))
    if rect_inicial_dois and tela1:
        rect2 = pygame.draw.rect(screen, cor_rect,(381,445,166,58))
        screen.blit(text_instrucoes,(383,462))
    if rect_inicial_tres and tela1:
        rect3 = pygame.draw.rect(screen, cor_rect,(381,515,166,58))
        screen.blit(text_creditos,(400, 532))
    if rect_creditos and tela3:
        rect7 = pygame.draw.rect(screen, cor_rect,(752,501,166,58))
        screen.blit(text_voltar,(789,519))
    if rect_instrucoes and tela4:
        rect9 = pygame.draw.rect(screen, cor_rect,(752,501,166,58))
        screen.blit(text_voltar,(789,519))
    if rect_jogar and tela2:
        rect11 = pygame.draw.rect(screen, cor_rect,(752,501,166,58))
        screen.blit(text_voltar,(789,519))

    #Posição do mouse   
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #Verificando se o mouse está em cima dos botões pra aplicar o efeito
    if (380< mouse_x <550) and (375< mouse_y <435) and tela1:
        cor_rect = verde
        rect_inicial_um = True
        rect_inicial_dois = False
        rect_inicial_tres = False
    elif (380< mouse_x <550) and (445< mouse_y <505) and tela1:
        cor_rect = verde
        rect_inicial_dois = True
        rect_inicial_um = False
        rect_inicial_tres = False
    elif (380< mouse_x <550) and (515< mouse_y <575) and tela1:
        cor_rect = verde
        rect_inicial_tres = True
        rect_inicial_um = False
        rect_inicial_dois = False
    elif (751< mouse_x <920) and (501< mouse_y <561) and tela3:
        cor_rect = verde
        rect_creditos = True
    elif (751< mouse_x <920) and (501< mouse_y <561) and tela4:
        cor_rect = verde
        rect_instrucoes = True
    elif (751< mouse_x <920) and (501< mouse_y <561) and tela2:
        cor_rect = verde
        rect_jogar = True
    else:
        cor_rect = preto
   
    pygame.display.flip()


#Fechando o Pygame
pygame.quit()
sys.exit()
    
