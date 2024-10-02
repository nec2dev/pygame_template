# pip install pygame# 
# # Importar e inicializar Pygame.
import pygame
pygame.init()
# Crear la ventana y poner el tamaño.
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
# Poner el título de la ventana.
pygame.display.set_caption("PES 2024")
# definir un icono y agregarlo a la ventana
icon = pygame.image.load("img/videogame.png")
pygame.display.set_icon(icon)
# Crear la superficie del fondo o background.
imgBackground = pygame.Surface(screen.get_size())
imgBackground = imgBackground.convert()
imgBackground.fill((0, 255, 0))
# Inicializar las variables de control del game loop.
clock = pygame.time.Clock()
salir = False
# Loop principal (game loop) del juego.
while not salir:
    # Timer que controla el frame rate.
    clock.tick(60)
    # Procesar los eventos que llegan a la aplicación.
    for event in pygame.event.get():
        # Si se cierra la ventana se sale del programa.
        if event.type == pygame.QUIT:
            # Si se pulsa la tecla [Esc] se sale del programa.
            salir = True
        if event.type ==  pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                 salir = True
    # Actualizar la pantalla.
    screen.blit(imgBackground, (0, 0))
    pygame.display.flip()
# Cerrar Pygame y liberar los recursos que pidió el programa.
pygame.quit()
