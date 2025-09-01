import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from AsteroidField import AsteroidField

def main():
    #Inicializa Pygame
    pygame.init()
    
    #Genera la ventana en donde se verá el juego, y asigna sus dimensiones según las variables importadas
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Genera el objeto "clock" que lleva registro del tiempo transcurrido
    clock = pygame.time.Clock()

    #Crear grupos a los que serán asignados los objetos
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    #Crea una variable de clase en los objetos para agruparlo en los grupos correspondientes
    Player.containers = (updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    #Crea una instancia de jugador y la centra en la pantalla
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    #Guarda el delta time, que guarda el tiempo que ha pasado desde el ultimo frame
    dt = 0
    
    while True:
        #Cierra la ventana y termina el loop si se apreta el boton X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Actualiza inputs y estados de los objetos
        updatable.update(dt)

        for object in asteroids:
            if object.collision(player) == True:
                print("Game over!")
                sys.exit()
        
        #Hace que la pantalla se coloree de negro cada frame
        screen.fill("black")

        #Dibuja todo lo dibujable en la pantalla
        for object in drawable:
            object.draw(screen)
        
        #Actualiza el contenido de toda la ventana de display
        pygame.display.flip()

        #limitar frames a 60 FPS
        dt = clock.tick(60) / 1000
        
    
        

if __name__ == "__main__":
    main()
