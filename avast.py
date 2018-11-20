import pygame, os, time, sys

pygame.init()

x = 855
y = 795

avast = pygame.image.load(os.path.join("Imagens","avast.png"))
avt = pygame.mixer.music.load(os.path.join("Musica","Avast.mp3"))

pygame.mixer.music.play()

os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' %(x,y)

screen = pygame.display.set_mode((508,234),pygame.NOFRAME)
screen.blit(avast,(0,0))
pygame.display.flip()

while y >= 495:
    pygame.display.quit()
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' %(x,y)
    screen = pygame.display.set_mode((508,234),pygame.NOFRAME)
    screen.blit(avast,(0,0))
    pygame.display.flip()
    time.sleep(0.05)
    y -= 30

time.sleep(5)

pygame.quit()
sys.exit()
