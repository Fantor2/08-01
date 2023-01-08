import pygame
import sys
 
# здесь определяются константы,
# классы и функции
FPS = 60
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1000
STACK_WIDTH = 20
STACK_HEIGHT = 120
STACK_OFFSET = 30
STICK_WIDTH = 20
STICK_HEIGHT = 120
STICK_OFFSET = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

def point_in_rect(pointx, pointy, rectx, recty , rect_width, rect_height):
    inx = rectx <= pointx <=rectx + rect_width
    iny = recty <=pointy <=recty + rect_height
    return inx and iny
# здесь происходит инициация,
# создание объектов
pygame.init()
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# радиус мяча
r = 20
# координаты мяча
ball_x = SCREEN_WIDTH//2
ball_y = SCREEN_HEIGHT // 2
# скорости мяча
ball_speed_x = 5
ball_speed_y = 4
#Кординаты ракетки
stack_x=STACK_OFFSET
stack_y= (SCREEN_HEIGHT - STACK_HEIGHT) // 2
stick_x =STICK_OFFSET
stick_y =(SCREEN_HEIGHT - STICK_HEIGHT) // 2
#скорость ракетки
stick_speed_y =0
stack_speed_y = 0
#
f2= pygame.font.Sysfront('algerian', 48)
left_score = 0
right_score = 0
# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    # --------
    # изменение объектов
    # --------
    # передвигаем мяч по экрану
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    # Выход за края экрана
    # левый
    if ball_x <= r:
        # летел налево - полетел направо
        ball_speed_x = -ball_speed_x
        right_score +=1
    # правый
    if ball_x >= SCREEN_WIDTH - r:
        # летел направо - полетел налево
        ball_speed_x = -ball_speed_x
        left_score +=1
    #Верхний
    if ball_y <=r:
        ball_speed_y = -ball_speed_y
    #Нижний
    if ball_y >= SCREEN_HEIGHT - r:
        ball_speed_y = -ball_speed_y
    #передвигаем ракетку по экрану
        stack_y +=stack_speed_y
    if stack_y <=0:
        stack_y =0
    elif stack_y >= SCREEN_HEIGHT - STACK_HEIGHT:
        stick_y = SCREEN_HEIGHT - STACK_HEIGHT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        stack_y -= 15
    elif keys[pygame.K_DOWN]:
        stack_y += 15
        
    stick_y +=stick_speed_y
    if stick_y <=0:
        stick_y =0
    elif stick_y >= SCREEN_HEIGHT - STICK_HEIGHT:
        stick_y = SCREEN_HEIGHT - STICK_HEIGHT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        stick_y -= 15
    elif keys[pygame.K_DOWN]:
        stick_y += 15
    #проверяем что мяч попал в ракетку
    #вычисляем середины сторон квадрата, описанного вокруг мяча
    mid_leftx=ball_x - r
    mid_lefty=ball_y
    
    mid_rightx=ball_x + r
    mid_righty=ball_y
    
    mid_topx= ball_x
    mid_topy= ball_y -r
    
    mid_bottomx = ball_x
    mid_bottomy = ball_y + r
    #правая граница ракетки
    if point_in_rect(mid_leftx, mid_lefty , stick_x , stick_y , STICK_WIDTH, STICK_HEIGHT):
        ball_speed_x = -ball_speed_x
    #верхняя граница ракетки
    if point_in_rect(mid_bottomx, mid_bottomy , stick_x , stick_y , STICK_WIDTH, STICK_HEIGHT):
        ball_speed_y = -ball_speed_y
    #нижняя граница ракетки
    if point_in_rect(mid_topx, mid_topy , stick_x , stick_y , STICK_WIDTH, STICK_HEIGHT):
        ball_speed_y = -ball_speed_y
    # обновление экрана
    # заливаем фон
    sc.fill(BLACK)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    pygame.draw.rect(sc,ORANGE, (stick_x, stick_y, STICK_WIDTH, STICK_HEIGHT))
    pygame.draw.rect(sc,ORANGE, (stack_x, stack_y, STACK_WIDTH, STACK_HEIGHT))
    pygame.display.update()
