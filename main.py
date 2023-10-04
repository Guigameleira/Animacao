import pygame , sys
from pygame.locals import QUIT
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width ,height))
hero_walk = []
hero_anim_frame = 1
hero_pos_x = 100
hero_pos_y = 225
hero_anim_time = 0
mapa = ['GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
        'GGGGGGGGGGGLLLLGGGGGGGGGGG',
       ]
def load():
  global clock, hero_walk, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M0, collider_mapa,collider_mapa1,collider_mapa2,collider_mapa3,collider_rio2,collider_rio4,collider_rio1,collider_rio3
  clock = pygame.time.Clock()
  collider_mapa = pygame.Rect(0, 0, 1, 600)
  collider_mapa1 = pygame.Rect(700, 0, 1, 600)
  collider_mapa2 = pygame.Rect(0,0,700,1)
  collider_mapa3 = pygame.Rect(0,550,700,1)
  collider_rio2 = pygame.Rect(250,300,90,300)
  collider_rio4=  pygame.Rect(250,300,1,300)
  collider_rio1 = pygame.Rect(250,0,1,100)
  collider_rio3 = pygame.Rect(2,0,1,100)
  M1 = pygame.image.load("source/CASA.png")
  M1 = pygame.transform.scale (M1, (200, 200))
  M2 = pygame.image.load("source/IGREJA.png")
  M2 = pygame.transform.scale (M2, (200, 200))
  M3 = pygame.image.load("source/POCO.png")
  M3 = pygame.transform.scale (M3, (50, 50))
  M4 = pygame.image.load("source/PONTE.png")
  M4 = pygame.transform.scale (M4, (180, 100))
  M5 = pygame.image.load("source/PLANTA.png")
  M5 = pygame.transform.scale (M5, (100, 100))
  M6 = pygame.image.load("source/PLANTA.png")
  M6 = pygame.transform.scale (M6, (100, 100))
  M7 = pygame.image.load("source/PLANTA.png")
  M7 = pygame.transform.scale (M7, (100, 100))
  M8 = pygame.image.load("source/PLANTA.png")
  M8 = pygame.transform.scale (M8, (100, 100))
  M9 = pygame.image.load("source/PLANTA2.png")
  M9 = pygame.transform.scale (M9, (50, 50))
  M10 = pygame.image.load("source/PLANTA2.png")
  M10 = pygame.transform.scale (M10, (50, 50))
  M0 = pygame.image.load("source/stairs.png")
  M0 = pygame.transform.scale (M0, (50, 50))
  
  for i in range(1, 9):
    hero_walk.append(pygame.image.load("source/Hero_Walk_0" + str(i) + ".png"))
  for i in range(0,6):
    hero_walk.append(pygame.image.load("source/Hero_Walk_1" + str(i) + ".png"))
   

def update(dt):
  global hero_walk, hero_anim_frame, hero_pos_x, hero_anim_time , hero_pos_y
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    hero_anim_time += 0.1 * dt
    hero_pos_x += (0.1 * dt)
    hero_anim_frame += 1
    if hero_anim_frame > 3:
        hero_anim_frame = 0
  if keys[pygame.K_LEFT]:
    hero_pos_x += (-0.1 * dt)
    hero_anim_frame += 1
    if hero_anim_frame > 7:
        hero_anim_frame = 4
  if keys[pygame.K_UP]:
    hero_pos_y -= 0.1 * dt
    hero_anim_frame += 1
    if hero_anim_frame > 10:
      hero_anim_frame = 8
  if keys[pygame.K_DOWN]:
    hero_pos_y += 0.1 * dt
    hero_anim_frame += 1
    if hero_anim_frame > 13:
      hero_anim_frame = 11

  collider_jogador = pygame.Rect(hero_pos_x, hero_pos_y, 100, 100)

  if collider_jogador.colliderect(collider_mapa):
        collider_jogador.left = collider_mapa.right
        hero_pos_x = collider_jogador.x

  if collider_jogador.colliderect(collider_mapa1):
        collider_jogador.right = collider_mapa1.left
        hero_pos_x = collider_jogador.x

  if collider_jogador.colliderect(collider_mapa2):
        collider_jogador.top = collider_mapa2.bottom
        hero_pos_y = collider_jogador.y
    
  if collider_jogador.colliderect(collider_mapa3):
        collider_jogador.bottom = collider_mapa3.top
        hero_pos_y = collider_jogador.y
    
  if collider_jogador.colliderect(collider_rio2):
        collider_jogador.left = collider_rio2.right
        hero_pos_x = collider_jogador.x

  if collider_jogador.colliderect(collider_rio4):
        collider_jogador.right = collider_rio4.left
        hero_pos_x = collider_jogador.x

  if collider_jogador.colliderect(collider_rio1):
        collider_jogador.left = collider_rio1.right
        hero_pos_x = collider_jogador.x

  if collider_jogador.colliderect(collider_rio3):
        collider_jogador.right = collider_rio3.left
        hero_pos_x = collider_jogador.x

def draw_screen(screen):
  
  for i,l in enumerate(mapa):
    for j,c in enumerate(l):
      if c == 'G':
        pygame.draw.rect(screen,(70, 242, 70), (30*j, 30*i,60,60))
      elif c == 'L':
        pygame.draw.rect(screen,(0, 170, 255), (30*j, 30*i,60,60))
  
  screen.blit(M0, (625, 220))
  screen.blit(M1, (550, 20))
  screen.blit(M2, (20, 20))
  screen.blit(M3, (230, 20))
  screen.blit(M4, (300, 250))
  screen.blit(hero_walk[hero_anim_frame], (hero_pos_x, hero_pos_y))
  screen.blit(M5, (20, 450))
  screen.blit(M6, (650, 450))
  screen.blit(M7, (170, 450))
  screen.blit(M8, (500, 450))
  screen.blit(M9, (260, 120))
  screen.blit(M10, (470, 120))

load()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    clock.tick(10)
    dt = clock.get_time()
    update(dt)
    draw_screen(screen)
    pygame.display.update()
