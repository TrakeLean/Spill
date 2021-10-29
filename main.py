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

clock = pygame.time.Clock()
pos_y = screenH/2
pos_x = screenW/2
model_size = [64*0.75,120*0.75]
pos_vel = 10
velocity = 0
dash_vel = pos_vel*1.5
walkCount = 0
walk_ = False
idle_ = False
hit_ = False
left_ = False
right = False



# walk_ = pygame.transform.scale(walk[walkCount//3],(model_size[0],model_size[1]))
# idle_ = pygame.transform.scale(idle[walkCount//3],(model_size[0],model_size[1]))
# hit_ = pygame.transform.scale(hit[walkCount//3],(model_size[0],model_size[1]))
pygame.display.set_caption("Sverd, Wallah... Schwing!")
icon = pygame.image.load('./sprites/tiles/176_224.png')
pygame.display.set_icon(icon)


#Text through GUI
myFont = pygame.font.SysFont("Times New Roman", 18)

def debug():
  
  # Animation status
  anim_text = myFont.render('Active Animation: ', True, black)
  anim_value = myFont.render(anim_stat, True, black)
  rect_anim = anim_text.get_rect()
  rect_anim.topleft = (20,20)
  
  screen.blit(anim_text,rect_anim)
  screen.blit(anim_value,(rect_anim[0]+140,rect_anim[1]))
  
  # Velocity
  speed = myFont.render('{}'.format(abs(velocity)), True, black)
  rect_speed = speed.get_rect()
  rect_speed.topleft = (20,40)
  
  screen.blit(speed,rect_speed)
  
  # Coordinates
  # x
  coord_x_text = myFont.render('X: ', True, black)
  coord_x = myFont.render('{}'.format(pos_x), True, black)
  rect_coord_x = coord_x_text.get_rect()
  rect_coord_x.topleft = (20,60)
  screen.blit(coord_x_text,rect_coord_x)
  screen.blit(coord_x,(rect_coord_x[0]*2,rect_coord_x[1]))
  # y
  coord_y_text = myFont.render('Y: ', True, black)
  coord_y = myFont.render('{}'.format(pos_y), True, black)
  screen.blit(coord_y_text,(rect_coord_x[0],rect_coord_x[1]+20))
  screen.blit(coord_y,(rect_coord_x[0]*2,rect_coord_x[1]+20))


def redrawGameWindow(walk,idle,hit):
  global walkCount, anim_stat
  screen.fill((88, 55, 24))
  
  if walkCount + 1 >= 13:
    walkCount = 0
    
  if walk_ == True:
    walk = pygame.transform.scale(walk[walkCount//3],(model_size[0],model_size[1]))
    if left_ == True:
      walk = pygame.transform.flip(walk,True,False)
    screen.blit(walk,(pos_x,pos_y))
    walkCount += 1
    anim_stat = "Walking"
    
    
  if idle_ == True:
    idle = pygame.transform.scale(idle[walkCount//3],(model_size[0],model_size[1]))
    if left_ == True:
      idle = pygame.transform.flip(idle,True,False)
    screen.blit(idle,(pos_x,pos_y))
    walkCount += 1
    anim_stat = "Idle"

  if hit_ == True:
    hit = pygame.transform.scale(hit[walkCount//3],(model_size[0],model_size[1]))
    screen.blit(hit,(pos_x,pos_y))
    walkCount += 1
    anim_stat = "Hit"
  
  debug()
  pygame.display.update()





# Game loop
running = True
while running:
  
  clock.tick(20)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_a] and pos_x > pos_vel-11:  
    pos_x_temp = pos_x
    pos_x = pos_x - pos_vel
    (velocity) = pos_x - pos_x_temp
    right = False
    left_ = True
    if keys[pygame.K_SPACE]:
      pos_x_temp = pos_x
      pos_x -= dash_vel
      velocity = pos_x - pos_x_temp

  if keys[pygame.K_d] and pos_x < screenW-model_size[0]:
    pos_x_temp = pos_x
    pos_x = pos_x + pos_vel
    velocity = pos_x - pos_x_temp
    left_ = False
    right = True
    if keys[pygame.K_SPACE]:
      pos_x_temp = pos_x
      pos_x += dash_vel
      velocity = pos_x - pos_x_temp

                
  if keys[pygame.K_w] and pos_y > pos_vel-44:
    pos_y_temp = pos_y
    pos_y = pos_y - pos_vel
    velocity = pos_y - pos_y_temp
    if keys[pygame.K_SPACE]:
      pos_y_temp = pos_y
      pos_y -= dash_vel
      velocity = pos_y - pos_y_temp

    
  if keys[pygame.K_s] and pos_y < screenH-model_size[1]:
    pos_y_temp = pos_y
    pos_y = pos_y + pos_vel
    velocity = pos_y - pos_y_temp
    if keys[pygame.K_SPACE]:
      pos_y_temp = pos_y
      pos_y += dash_vel
      velocity = pos_y - pos_y_temp
      
  if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
    idle_ = False
    walk_ = True
  else:
    walk_ = False
    idle_ = True
    velocity = 0
    
  redrawGameWindow(walk,idle,hit)

