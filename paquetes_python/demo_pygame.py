import pygame
#se inicializa la libreria
pygame.init()
#mostrar la ventna GUI
window = pygame.display.set_mode((500,400))
while True:
    pygame.draw.lines(window,(0,255,255), True,((50,50),(75,75),(63,100),(38,100),(25,75)),3)
    pygame.display.update()