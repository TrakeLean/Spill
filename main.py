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

walk = [pygame.image.load('./sprites/denne/character/wizzard_m_run_anim_f0.png'),
        pygame.image.load('./sprites/denne/character/wizzard_m_run_anim_f1.png'),
        pygame.image.load('./sprites/denne/character/wizzard_m_run_anim_f2.png'),
        pygame.image.load('./sprites/denne/character/wizzard_m_run_anim_f3.png')]

idle = [pygame.image.load('./sprites/denne/character/wizzard_m_idle_anim_f0.png'),
        pygame.image.load('./sprites/denne/character/wizzard_m_idle_anim_f1.png'),
        pygame.image.load('./sprites/denne/character/wizzard_m_idle_anim_f2.png'),
        pygame.image.load('./sprites/denne/character/wizzard_m_idle_anim_f3.png')]

hit = [pygame.image.load('./sprites/denne/character/wizzard_m_hit_anim_f0.png')]


# Window
screenW=1200
screenH=800
screen = pygame.display.set_mode((screenW,screenH))
pos_y = screenH/2
pos_x = screenW/2
model_size = [64,120]
pos_vel = 10
jump_vel = 3
walkCount = 0
walk_ = False
idle_ = False
hit_ = False



# walk_ = pygame.transform.scale(walk[walkCount//3],(model_size[0],model_size[1]))
# idle_ = pygame.transform.scale(idle[walkCount//3],(model_size[0],model_size[1]))
# hit_ = pygame.transform.scale(hit[walkCount//3],(model_size[0],model_size[1]))
pygame.display.set_caption("Sverd, Wallah... Schwing!")
icon = pygame.image.load('./sprites/tiles/176_224.png')
pygame.display.set_icon(icon)






def redrawGameWindow(walk,idle,hit):
  global walkCount
  screen.fill((88, 55, 24))
  
  if walkCount + 1 >= 12:
    walkCount = 0
    
  if walk_ == True:
    walk = pygame.transform.scale(walk[walkCount//3],(model_size[0],model_size[1]))
    screen.blit(walk,(pos_x,pos_y))
    walkCount += 1
    
  if idle_ == True:
    idle = pygame.transform.scale(idle[walkCount//3],(model_size[0],model_size[1]))
    screen.blit(idle,(pos_x,pos_y))
    walkCount += 1

  if hit_ == True:
    hit = pygame.transform.scale(hit[walkCount//3],(model_size[0],model_size[1]))
    screen.blit(hit,(pos_x,pos_y))
    walkCount += 1
    
  pygame.display.update()





# Game loop
running = True
while running:

  
  pygame.time.delay(50)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_a] and pos_x > pos_vel-11:
    idle_ = False
    walk_ = True
    pos_x = pos_x - pos_vel
    if keys[pygame.K_SPACE]:
      pos_x -= jump_vel


  if keys[pygame.K_d]and pos_x < screenW-model_size[0]:
    idle_ = False
    walk_ = True
    pos_x = pos_x + pos_vel
    if keys[pygame.K_SPACE]:
      pos_x += jump_vel

                
  if keys[pygame.K_w]and pos_y > pos_vel-44:
    idle_ = False
    walk_ = True
    pos_y = pos_y - pos_vel
    if keys[pygame.K_SPACE]:
      pos_y -= jump_vel    

    
  if keys[pygame.K_s]and pos_y < screenH-model_size[1]:
    idle_ = False
    walk_ = True
    pos_y = pos_y + pos_vel
    if keys[pygame.K_SPACE]:
      pos_y += jump_vel
  else:
    walkCount += 1
    walk_ = False
    idle_ = True
    
    
  redrawGameWindow(walk,idle,hit)

