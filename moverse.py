import pygame, turtle

pygame.init()
screen = pygame.display.set_mode((500, 350))
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        print('hola')
        turtle.fd(10)
    if keys[pygame.K_LEFT]:
        print('adios')
        turtle.fd(-10)