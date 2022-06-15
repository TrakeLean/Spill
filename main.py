import pygame
from pygame import display
from pygame.constants import K_LEFT, K_d
import random


pygame.init()
clock = pygame.time.Clock()



class enemy(object):
  def __init__(self,pos_x,pos_y,width,height):
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.width = width
    self.height = height
    self.pos_vel = 5
    self.dash_vel = self.pos_vel*1.25
    self.walkCount = 0
    self.walk_ = True
    self.walk = [pygame.image.load('./sprites/denne/enemy/necromancer_run_anim_f0.png'),
                pygame.image.load('./sprites/denne/enemy/necromancer_run_anim_f1.png'),
                pygame.image.load('./sprites/denne/enemy/necromancer_run_anim_f2.png'),
               pygame.image.load('./sprites/denne/enemy/necromancer_run_anim_f3.png')]

    self.idle = [pygame.image.load('./sprites/denne/enemy/necromancer_idle_anim_f0.png'),
                 pygame.image.load('./sprites/denne/enemy/necromancer_idle_anim_f1.png'),
                 pygame.image.load('./sprites/denne/enemy/necromancer_idle_anim_f2.png'),
                 pygame.image.load('./sprites/denne/enemy/necromancer_idle_anim_f3.png')]

    self.hit = [pygame.image.load('./sprites/denne/character/wizzard_m_hit_anim_f0.png')]
  
  def draw(self,screen):
    if self.walkCount + 1 >= 13:
      self.walkCount = 0
    
    if self.walk_ == True:
      walk = pygame.transform.scale(self.walk[self.walkCount//3],(self.width,self.height))
      screen.blit(walk,(self.pos_x,self.pos_y))
      self.walkCount += 1





class player(object):
  def __init__(self,pos_x,pos_y,width,height):
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.width = width
    self.height = height
    self.pos_vel = 5
    self.velocity = 0
    self.dash_vel = self.pos_vel*1.20
    self.walkCount = 0
    self.anim_stat = "Debug pls..."
    self.walk_ = False
    self.idle_ = False
    self.hit_ = False
    self.left_ = False
    self.right_ = False
    self.up_ = False
    self.down_ = False
    self.rot = 0
    self.walk = [pygame.image.load('./sprites/denne/character/wizzard_m_run_anim_f0.png'),
                pygame.image.load('./sprites/denne/character/wizzard_m_run_anim_f1.png'),
                pygame.image.load('./sprites/denne/character/wizzard_m_run_anim_f2.png'),
                pygame.image.load('./sprites/denne/character/wizzard_m_run_anim_f3.png')]

    self.faceup = [pygame.image.load('./sprites/denne/character/wizzard_m_faceup_anim_f0.png'),
                pygame.image.load('./sprites/denne/character/wizzard_m_faceup_anim_f1.png'),
                pygame.image.load('./sprites/denne/character/wizzard_m_faceup_anim_f2.png'),
                pygame.image.load('./sprites/denne/character/wizzard_m_faceup_anim_f3.png')]

    self.idle = [pygame.image.load('./sprites/denne/character/wizzard_m_idle_anim_f0.png'),
                pygame.image.load('./sprites/denne/character/wizzard_m_idle_anim_f1.png'),
                pygame.image.load('./sprites/denne/character/wizzard_m_idle_anim_f2.png'),
                pygame.image.load('./sprites/denne/character/wizzard_m_idle_anim_f3.png')]

    self.hit = [pygame.image.load('./sprites/denne/character/wizzard_m_hit_anim_f0.png')]
  
  def draw(self,screen):
    if self.walkCount + 1 >= 13:
      self.walkCount = 0
    
    if self.walk_ == True:
      walk = pygame.transform.scale(self.walk[self.walkCount//3],(self.width,self.height))
      if self.left_ == True:
        walk = pygame.transform.flip(walk,True,False)
      screen.blit(walk,(self.pos_x,self.pos_y))
      self.walkCount += 1
      self.anim_stat = "Walking"
      
    if self.up_ == True:
      faceup = pygame.transform.scale(self.faceup[self.walkCount//6],(64,100))
      screen.blit(faceup,(self.pos_x,self.pos_y+20))
      self.walkCount += 1
      self.anim_stat = "Walking"
      
      
    if self.idle_ == True:
      idle = pygame.transform.scale(self.idle[self.walkCount//3],(self.width,self.height))
      if self.left_ == True:
        idle = pygame.transform.flip(idle,True,False)
      screen.blit(idle,(self.pos_x,self.pos_y))
      self.walkCount += 1
      self.anim_stat = "Idle"

    if self.hit_ == True:
      hit = pygame.transform.scale(self.hit[self.walkCount//3],(self.width,self.height))
      screen.blit(hit,(self.pos_x,self.pos_y))
      self.walkCount += 1
      self.anim_stat = "Hit"



class projectile(object):
  def __init__(self,x,y,facing_x,facing_y):
    self.x = x
    self.y = y
    self.facing_x = facing_x
    self.facing_y = facing_y
    self.velocity = 2
    self.velocity_x = self.velocity * self.facing_x
    self.velocity_y = self.velocity * self.facing_y
    self.moving = [pygame.image.load('./sprites/customsprites/tile001.png'),
                   pygame.image.load('./sprites/customsprites/tile002.png'),
                   pygame.image.load('./sprites/customsprites/tile003.png')]
    
  def draw(self,screen):
    moving = pygame.transform.scale(self.moving[hero.walkCount//5],(32*3,32*3))
    moving = pygame.transform.rotate(moving,hero.rot)

      
    screen.blit(moving,(self.x,self.y))
    
  def move(self):
    if hero.left_ == True:
        self.x += self.velocity_x
    if hero.right_ == True:
        self.x += self.velocity_x
    if hero.up_ == True:
        self.y += self.velocity_y
    if hero.down_ == True:
        self.y += self.velocity_y
  




# Window
screenW=1200
screenH=800
screen = pygame.display.set_mode((screenW,screenH))
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)



pygame.display.set_caption("Sverd, Wallah... Schwing!")
icon = pygame.image.load('./sprites/tiles/176_224.png')
pygame.display.set_icon(icon)


#Text through GUI
myFont = pygame.font.SysFont("Times New Roman", 18)

def debug():
  color = white
  # Animation status
  anim_text = myFont.render('Active Animation: ', True, color)
  anim_value = myFont.render(hero.anim_stat, True, color)
  rect_anim = anim_text.get_rect()
  rect_anim.topleft = (20,20)
  
  screen.blit(anim_text,rect_anim)
  screen.blit(anim_value,(rect_anim[0]+140,rect_anim[1]))
  
  # Velocity
  speed = myFont.render('{}'.format(abs(hero.velocity)), True, color)
  rect_speed = speed.get_rect()
  rect_speed.topleft = (20,40)
  
  screen.blit(speed,rect_speed)
  
  # Coordinates
  # x
  coord_x_text = myFont.render('X: ', True, color)
  coord_x = myFont.render('{}'.format(hero.pos_x), True, color)
  rect_coord_x = coord_x_text.get_rect()
  rect_coord_x.topleft = (20,60)
  screen.blit(coord_x_text,rect_coord_x)
  screen.blit(coord_x,(rect_coord_x[0]*2,rect_coord_x[1]))
  # y
  coord_y_text = myFont.render('Y: ', True, color)
  coord_y = myFont.render('{}'.format(hero.pos_y), True, color)
  screen.blit(coord_y_text,(rect_coord_x[0],rect_coord_x[1]+20))
  screen.blit(coord_y,(rect_coord_x[0]*2,rect_coord_x[1]+20))




  

def redrawGameWindow():
  #screen.fill((88, 55, 24))
  background = pygame.image.load('./sprites/background.png')
  background = pygame.transform.scale(background,(screenW,screenH))
  screen.blit(background,(0,0))
  hero.draw(screen)
  enemy.draw(screen)
  for bullet in bullets:
    bullet.draw(screen)
  debug()

  pygame.display.update()





# Game loop
hero = player(screenW/2,screenH/2,64,120)
enemy = enemy(screenW/2,screenH/2,64,64)
bullets = []
running = True
while running:
  keys = pygame.key.get_pressed()
  
  clock.tick(20)
  for event in pygame.event.get():
    if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
      running = False
    if running == False:
      pygame.quit()

  for bullet in bullets:
    if bullet.x < screenW and bullet.x > 0 and bullet.y < screenH and bullet.y > 0 :
      bullet.move()
    else:
      bullets.pop(bullets.index(bullet))

  
  if keys[pygame.K_SPACE] and (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]):
    facing_x = 0
    facing_y = 0
    
    if keys[pygame.K_a]:
      facing_x = -1
      hero.rot = 90
    if keys[pygame.K_d]:
      hero.rot = -90
      facing_x = 1
    if keys[pygame.K_w]:
      hero.rot = 0
      facing_y = -1
    if keys[pygame.K_s]:
      hero.rot = 180
      facing_y = 1
    if keys[pygame.K_s] and keys[pygame.K_a]:
      hero.rot = 135
    if keys[pygame.K_s] and keys[pygame.K_d]:
      hero.rot = 225
    if keys[pygame.K_w] and keys[pygame.K_a]:
      hero.rot = 45
    if keys[pygame.K_w] and keys[pygame.K_d]:
      hero.rot = -45


        

      
    if len(bullets) <= 700:
      bullets.append(projectile(round(hero.pos_x + hero.width//3), round(hero.pos_y + hero.height), facing_x, facing_y))
    else:
      pass
      
  
  if keys[pygame.K_a] and hero.pos_x > hero.pos_vel-11:  
    pos_x_temp = hero.pos_x
    hero.pos_x = hero.pos_x - hero.pos_vel
    hero.velocity = hero.pos_x - pos_x_temp
    hero.up_ = False
    hero.right_ = False
    hero.left_ = True
    if keys[pygame.K_LSHIFT]:
      pos_x_temp = hero.pos_x
      hero.pos_x -= hero.dash_vel
      hero.velocity = hero.pos_x - pos_x_temp

  if keys[pygame.K_d] and hero.pos_x < screenW-hero.width:
    pos_x_temp = hero.pos_x
    hero.pos_x = hero.pos_x + hero.pos_vel
    hero.velocity = hero.pos_x - pos_x_temp
    hero.up_ = False
    hero.left_ = False
    hero.right_ = True
    if keys[pygame.K_LSHIFT]:
      pos_x_temp = hero.pos_x
      hero.pos_x += hero.dash_vel
      hero.velocity = hero.pos_x - pos_x_temp

                
  if keys[pygame.K_w] and hero.pos_y > hero.pos_vel-44:
    pos_y_temp = hero.pos_y
    hero.pos_y = hero.pos_y - hero.pos_vel
    hero.velocity = hero.pos_y - pos_y_temp
    hero.idle_ = False
    hero.down_ = False
    hero.up_ = True
    if keys[pygame.K_LSHIFT]:
      pos_y_temp = hero.pos_y
      hero.pos_y -= hero.dash_vel
      hero.velocity = hero.pos_y - pos_y_temp

    
  if keys[pygame.K_s] and hero.pos_y < screenH-hero.height:    
    pos_y_temp = hero.pos_y
    hero.pos_y = hero.pos_y + hero.pos_vel
    hero.velocity = hero.pos_y - pos_y_temp
    hero.up_ = False
    hero.down_ = True
    if keys[pygame.K_LSHIFT]:
      pos_y_temp = hero.pos_y
      hero.pos_y += hero.dash_vel
      hero.velocity = hero.pos_y - pos_y_temp
      
  if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
    hero.idle_ = False
    hero.walk_ = True
  # else:
  #   hero.walk_ = False
  #   hero.idle_ = True
  #   hero.velocity = 0
    
  redrawGameWindow()

