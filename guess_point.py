import pygame,sys,random
from pygame.locals import *


def get_key(dir_point,value):
    a = [k for k,v in dir_point.items() if value in v]
    return a[0]

def get_list_point(point_set):
    list_point = []
    for i in range(len(point_set)):
        for j in range(len(point_set[0])):
            list_point.append([i,j])
    return list_point

def choose_target(list_point):
    length = len(list_point)
    target = random.randrange(length)
    return list_point[target]

def set_target(target,point_set):
    new_point_set = copy.deepcopy(point_set)
    new_point_set[target[0]][target[1]] = 1
    return new_point_set


def get_distance(target_point,point):
    distance = abs(point[0]-target_point[0])+abs(point[1]- target_point[1])
    return distance

def gameover():
    gameOverFont =pygame.font.Font('FiraCode.ttf',72)
    gameOverSurf = gameOverFont.render('Conguration', True, blackcolor)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320,5)
    retryfont = pygame.font.Font('FiraCode.ttf',50)
    retrysurf = retryfont.render('Press \'Y\' to restart', True, blackcolor)
    retryrect = retrysurf.get_rect()
    retryrect.midtop = (320,180)
    screen.blit(gameOverSurf,gameOverRect)
    screen.blit(retrysurf,retryrect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quitgame()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                if event.key == ord('y'):
                    game()

def quitgame():
    pygame.quit()
    sys.exit()

def game():
    global blackcolor
    global whitecolor
    global redcolor
    global bluecolor
    global screen
    pygame.init()
    screen = pygame.display.set_mode((640,640))
    blackcolor = pygame.Color(0,0,0)
    whitecolor = pygame.Color(255,255,255)
    redcolor = pygame.Color(255,0,0)
    bluecolor = pygame.Color(0,0,255)
    screen.fill(blackcolor)

    for i in range(0,640,80):
        for j in range(0,640,80):
            if (int(i/80)+int(j/80))%2 == 0:
                pygame.draw.rect(screen,redcolor,Rect(j,i,80,80))
            else:
                pygame.draw.rect(screen,whitecolor,Rect(j,i,80,80))

    # gamefont = pygame.font.SysFont('firacodettf',50)
    gamefont = pygame.font.Font('FiraCode.ttf',50)

    point_set = [[0 for i in range(8)] for  j in range(8)]
    list_point = get_list_point(point_set)
    target = choose_target(list_point)
    print(target)

    dir_point = {0:[i for i in range(0,81)],1:[i for i in range(81,161)], 2:[i for i in range(161,241)], 3:[i for i in range(241,321)],4:[i for i in range(321,401)],5:[i for i in range(401,481)], 6:[i for i in range(481,561)],7:[i for i in range(561,641)]}
    font_x = {25:[i for i in range(0,81)],105:[i for i in range(81,161)], 185:[i for i in range(161,241)], 265:[i for i in range(241,321)],345:[i for i in range(321,401)],425:[i for i in range(401,481)], 505:[i for i in range(481,561)],585:[i for i in range(561,641)]}
    font_y = {10:[i for i in range(0,81)],90:[i for i in range(81,161)], 170:[i for i in range(161,241)], 250:[i for i in range(241,321)],330:[i for i in range(321,401)],410:[i for i in range(401,481)], 490:[i for i in range(481,561)],570:[i for i in range(561,641)]}

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                for i in range(0,640,80):
                    for j in range(0,640,80):
                        if (int(i/80)+int(j/80))%2 == 0:
                            pygame.draw.rect(screen,redcolor,Rect(j,i,80,80))
                        else:
                            pygame.draw.rect(screen,whitecolor,Rect(j,i,80,80))
                x, y = pygame.mouse.get_pos()
                new_y = get_key(dir_point,x)
                new_x = get_key(dir_point,y)
                show_w_x= get_key(font_x,x)
                show_w_y = get_key(font_y,y)
                choose_point = [new_x,new_y]
                distance = get_distance(target,choose_point)
                font_surface = gamefont.render(str(distance),True,bluecolor)
                print(x)
                print(y)
                screen.blit(font_surface,(show_w_x,show_w_y))
                if distance == 0:
                    gameover()

        pygame.display.update()



game()