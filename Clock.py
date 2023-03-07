import pygame 
import time

pygame.init()

screen = pygame.display.set_mode((500,600))

GREY = (150,150,150)
WHITE = (250,250,250)
BLACK = (0,0,0)
RED = (255,0,0)

font = pygame.font.SysFont('sans', 50)
text_1 = font.render('+', True, BLACK)
text_2 = font.render('-', True, BLACK)
text_3 = font.render('+', True, BLACK)
text_4 = font.render('-', True, BLACK)
text_5 = font.render('Start', True, BLACK)
text_6 = font.render('Reset', True, BLACK)
time_out = font.render('TIME OUT', True, BLACK)


total_secs = 0
start = False

running = True

while running:
    screen.fill(GREY)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    pygame.draw.rect(screen, WHITE, (100,50,50,50))
    pygame.draw.rect(screen, WHITE, (100,200,50,50))
    pygame.draw.rect(screen, WHITE, (200,50,50,50))
    pygame.draw.rect(screen, WHITE, (200,200,50,50))
    pygame.draw.rect(screen, WHITE, (300,50,150,50))
    pygame.draw.rect(screen, WHITE, (300,150,150,50))
    

    screen.blit(text_1, (100,50))
    screen.blit(text_2, (100,200))
    screen.blit(text_3, (200,50))
    screen.blit(text_4, (200,200))
    screen.blit(text_5, (300,50))
    screen.blit(text_6, (300,150))
    screen.blit(time_out, (170,520))

    pygame.draw.rect(screen, BLACK, (50,520, 400,50))
    pygame.draw.rect(screen, WHITE, (60,530, 380,30))

    pygame.draw.circle(screen, BLACK, (250,400), 100)
    pygame.draw.circle(screen, WHITE, (250,400), 95)
    pygame.draw.circle(screen, BLACK, (250,400), 5)

    pygame.draw.line(screen, BLACK, (250,400), (250,310))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if(100 < mouse_x < 150) and (50 < mouse_y < 100):
                    total_secs += 60
                if(200 < mouse_x < 250) and (50 < mouse_y < 100):
                    total_secs += 1
                if(300 < mouse_x < 450) and (50 < mouse_y < 100):
                    start = True
                    print("press start")
                if(100 < mouse_x < 150) and (200 < mouse_y < 250):
                    total_secs -= 60
                if(200 < mouse_x < 250) and (200 < mouse_y < 250):
                    total_secs -= 1
                if(300 < mouse_x < 400) and (150 < mouse_y < 200):
                    total_secs = 0
                    print("press reset")
                print("total secs:" + str(total_secs))

    if start:
        total_secs -= 1
        if total_secs == 0:          
            start = False           
        time.sleep(1)
    
    if total_secs < 0:
        total_secs = 0

    mins = int(total_secs/60)
    secs = total_secs - mins*60

    time_now = str(mins) + ":" + str(secs)

    text_time = font.render(time_now, True, BLACK)
    screen.blit(text_time, (120,120))

    pygame.display.flip()

pygame.quit()