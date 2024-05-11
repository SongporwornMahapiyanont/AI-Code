import pygame

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Hello")

BLACK = (0,0,0)
display_surface.fill(BLACK)

bg = pygame.image.load("beach_sun.jpg")
bg = pygame.transform.scale(bg, (WINDOW_WIDTH,WINDOW_HEIGHT))
bg_rect = bg.get_rect()
bg_rect.topleft = (0,0)

dog = pygame.image.load("dog.png")
dog = pygame.transform.scale(dog, (168,260))
dog_rect = dog.get_rect()
dog_rect.topleft = (300,120)

tree = pygame.image.load("treeH.png")
tree = pygame.transform.scale(tree, (150,130))
tree_rect = tree.get_rect()
tree_rect.topleft = (100,250)

# The main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(bg,bg_rect)
    display_surface.blit(tree,tree_rect)    
    display_surface.blit(dog,dog_rect)
    
    pygame.display.update()

pygame.quit()
