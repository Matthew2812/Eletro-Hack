import pygame,time,os, sys

pygame.init()

tela_azul = pygame.image.load(os.path.join('Imagens','tela-azul.jpg'))
tela_azul = pygame.transform.smoothscale(tela_azul,(1366,768))


screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen.blit(tela_azul,(0,0))
pygame.display.flip()

time.sleep(5)

pygame.quit()
sys.exit()
