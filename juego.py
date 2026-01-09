import sys #para usar exit()
import pygame

ancho = 640
alto = 480
color_azul = (0,0,64) #Color azul para el fondo.

class Bolita(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    # Cargar Imagen
    self.image = pygame.image.load("imagenes/bolita.png")
    # Escalar la imagen a 20x20 píxeles
    self.image = pygame.transform.scale(self.image, (20, 20))
    # Obtener rectangulo de la imagen
    self.rect = self.image.get_rect()
    # Posición inicial centrada en pantalla
    self.rect.centerx = ancho /2
    self.rect.centery = alto /2
    # Establecer velocidad inicial
    self.speed = [3,3]

  def update(self):
    # Evitar que salga por arriba o abajo
    if self.rect.bottom >= alto or self.rect.top <= 0:
      self.speed[1] = -self.speed[1]
    #  Evitar que salga por la derecha o izquierda
    elif self.rect.right >= ancho or self.rect.left <= 0:
      self.speed[0] = -self.speed[0]
    # Mover en base a posicion actual y velocidad
    self.rect.move_ip(self.speed)

class Paleta(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    # Cargar Imagen
    self.image = pygame.image.load("imagenes/paleta.png")
    # Escalar la imagen a 20x20 píxeles
    self.image = pygame.transform.scale(self.image, (60, 20))
    # Obtener rectangulo de la imagen
    self.rect = self.image.get_rect()
    # Posición inicial centrada en x
    self.rect.midbottom = (ancho /2, alto -20)
    # Establecer velocidad inicial
    self.speed = [0,0]
  def update(self,evento):
    # Buscar si se preciono flecha izquierda
    if evento.key == pygame.K_LEFT and self.rect.left > 0:
      self.speed = [-5,0]
    # si se preciono la flecha derecha
    elif evento.key == pygame.K_RIGHT and self.rect.right < ancho:
      self.speed = [5,0]
    else:
      self.speed = [0,0]
    # Mover en base a posicion actual y velocidad
    self.rect.move_ip(self.speed)

class Ladrillo(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    # Cargar Imagen
    self.image = pygame.image.load("imagenes/bolita.png")
    # Escalar la imagen a 20x20 píxeles
    self.image = pygame.transform.scale(self.image, (20, 20))
    # Obtener rectangulo de la imagen
    self.rect = self.image.get_rect()
    # Posición inicial centrada en pantalla
    self.rect.centerx = ancho /2
    self.rect.centery = alto /2
    # Establecer velocidad inicial
    self.speed = [3,3]

# Inicializando pantalla
pantalla = pygame.display.set_mode((ancho, alto))
# Configurar titulo de pantalla
pygame.display.set_caption("Juego de Ladrillos")
# Crear Reloj
reloj = pygame.time.Clock()
# Ajustar repeticion de evento de tecla presionada
pygame.key.set_repeat(30)

bolita = Bolita()
jugador = Paleta()

while True:
  # Establecer FPS
  reloj.tick(60)

  # Revisar todos los eventos
  for evento in pygame.event.get():
    # Si se presiona la barra de titulo
    if evento.type == pygame.QUIT:
      sys.exit()
    # Buscar eventos del teclado
    elif evento.type == pygame.KEYDOWN:
      jugador.update(evento)

  # Actualizar posicion de la bolita
  bolita.update()
  # Rellenar la pantalla.
  pantalla.fill(color_azul)
  # Dibujar la bolita en pantalla
  pantalla.blit(bolita.image, bolita.rect)
  # Dibujar jugador en pantalla
  pantalla.blit(jugador.image, jugador.rect)
  # Actualizar los elementos en pantalla
  pygame.display.flip()

