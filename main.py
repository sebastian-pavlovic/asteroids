import pygame
from constants import *
from player import Player

def main():
    #Inicializa Pygame
    pygame.init()
    
    print("Starting Asteroids!")
    
    #Genera la ventana en donde se verá el juego, y asigna sus dimensiones según las variables importadas
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Genera el objeto "clock" que lleva registro del tiempo transcurrido
    clock = pygame.time.Clock()
    #Guarda el delta time, que guarda el tiempo que ha pasado desde el ultimo frame
    dt = 0
    #Crea una instancia de jugador y la centra en la pantalla
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)

    while True:
        #Cierra la ventana y termina el loop si se apreta el boton X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Hace que la pantalla se coloree de negro cada frame
        screen.fill("black")
        #Dibuja al jugador en la pantalla
        player.draw(screen)
        #Actualiza el contenido de toda la ventana de display
        pygame.display.flip()

        #limitar frames a 60 FPS
        dt = clock.tick(60) / 1000
        
    
        

if __name__ == "__main__":
    main()
