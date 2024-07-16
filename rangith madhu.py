import pygame,sys

pygame.init()

screen = pygame.display.set_mode((500,500))
running = True
while(running):
    for event in pygame.event.get() :
        if event . type ==pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    screen.fill(pygame.color('green'))
    test_surface.fill((0,0,255))
    test_rect.right +=1
    screen.blit(test_surface,test_rect)
    pygame.display.update()
    clock.tick(60)
    
    
    
