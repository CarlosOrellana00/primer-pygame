import sys #para usar exit()
import pygame

ancho = 640
alto = 480

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

# Inicializando pantalla
pantalla = pygame.display.set_mode((ancho, alto))
# Configurar titulo de pantalla
pygame.display.set_caption("Juego de Ladrillos")

bolita = Bolita()

while True:
  # Revisar todos los eventos
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      sys.exit()

  #Dibujar la bolita en pantalla
  pantalla.blit(bolita.image, bolita.rect)
  # Actualizar los elementos en pantalla
  pygame.display.flip()

