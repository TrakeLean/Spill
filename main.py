import pygame
from pygame import display
from pygame.constants import K_LEFT, K_d

pygame.init()
clock = pygame.time.Clock()


# Define R G B
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)


# Window
screenW=1200
screenH=800
screen = pygame.display.set_mode((screenW,screenH))
pos_y = screenH/3
pos_x = screenW/3
image = pygame.image.load('./sprites/denne/character/wizzard_m_idle_anim_f0.png')
pygame.display.set_caption("Sverd, Wallah... Schwing!")
icon = pygame.image.load('./sprites/tiles/176_224.png')
pygame.display.set_icon(icon)


    
def player():
  screen.blit(image,(pos_x,pos_y))





# Game loop
running = True
while running:
  screen.fill((88, 55, 24))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()

  
  
  # Draw
  pygame.display.update()
  player()
  clock.tick(60)

  
  
  