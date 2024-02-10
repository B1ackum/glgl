import pygame
pygame.init()
CLOCK=pygame.time.Clock()
a = int(input("ENter: "))
b = int(input("ENter: "))
c=a+b
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 800
BG_COLOR = (255,255,255)
BLACK = (0,0,0)
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
screen.fill(BG_COLOR)
# imp=pygame.image.load("C:\\Users\\Think Engineering\\Pictures\\gmgm.png")
# screen.blit(imp, (-50, -50))
FPS = 60

font = pygame.font.Font('freesansbold.ttf', 100)
text = font.render(f"{c}", True, 'red')
screen.blit(text,(20,20))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    CLOCK.tick(FPS)
    text = font.render(str(a + b), True, BLACK)


    pygame.display.update()

