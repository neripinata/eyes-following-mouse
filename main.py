import time
import keyboard
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('EYES')
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True


        mousePosition = pygame.mouse.get_pos()
        x = mousePosition[0]
        y = mousePosition[1]

        if x < 280:
            x_1 = 280
        elif x > 360:
            x_1 = 360
        else:
            x_1 = x
        if y < 260:
            y_1 = 260
        elif y > 340:
            y_1 = 340
        else:
            y_1 = y



        if x < 450:
            x_2 = 450
        elif x > 530:
            x_2 = 530
        else:
            x_2 = x

        print(mousePosition)

        pygame.draw.circle(screen, (255,255,255), (320,300), 80)
        pygame.draw.circle(screen, (255,255,255), (490,300), 80)

        #circulo derecha
        pygame.draw.circle(screen, (255,255,0), (x_1,y_1), 40)
        #circulo pequeño izquierda
        pygame.draw.circle(screen, (255,255,0), (x_2,y_1), 40)

        #pygame.draw.circle(screen, (255,255,255), (x,y), 50)
        
        
        pygame.display.flip()
        screen.fill(pygame.Color("black"))



