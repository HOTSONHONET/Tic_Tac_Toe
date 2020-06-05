import pygame as pg, sys
from pygame.locals import *
import time


#INTRODUCING OUR GLOBAL VARIABLES
XO = 'x'
winner = None
width = 400
height = 400
draw = False
Blue = (255,255,255)
line_color = (10,10,10)

#OUR TIC_TAC_TOE_Board
TTT = [[None]*3,[None]*3,[None]*3]

#Initialising Pygame window
pg.init()
pg.font.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100),0,32)
pg.display.set_caption('TIC_TAC_TOE')


#LOADING IMAGES
opening_img = pg.image.load('images/opening_image.jpg')
X_img = pg.image.load('images/x.png')
O_img = pg.image.load('images/o.png')

#RESIZING OUR IMAGES
X_img = pg.transform.scale(X_img, (80,80))
O_img = pg.transform.scale(O_img, (80,80))
opening_img = pg.transform.scale(opening_img, (width, height + 100))


#OPERATING_UNIT
def game_opening():
    screen.blit(opening_img,(0,0))
    pg.display.update()
    time.sleep(2)
    screen.fill(Blue)

    #DRAWING VERTICAL LINES
    pg.draw.line(screen, line_color, [width/3, 0], [width/3, height], 7)
    pg.draw.line(screen, line_color, [(width*2)/3, 0], [(2*width)/3, height], 7 )

    #DRAWING HORIZONTAL LINES
    pg.draw.line(screen, line_color, [0,height/3], [width, height/3], 7)
    pg.draw.line(screen, line_color, [0,(2*height)/3], [width, (2*height)/3], 7)

    draw_status()

def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + " 's turn"

    else:
        message = winner.upper() + ' WINS'

    if draw :
        message = 'NoBODY WIN$'


    font = pg.font.SysFont("Arial", 30)
    text = font.render(message, 1, (255, 0, 0))



#Copying the rendering images on the board
    #screen.fill(color, rectangle(x,y, width, height))

    screen.fill((0, 0, 0), (0, 400, 500, 100))
    screen.blit(text, (width/3, 425))
    pg.display.update()

    #return text, text_rect



def check_win():
    global TTT, winner, draw

    #CHECKING FOR WINNING ROWS

    #1 HORIZONTALLY
    for row in range(0,3):
        if ((TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] != None)):
            winner = TTT[row][0]
            pg.draw.line(screen, (0, 250, 250), (0, (row + 1)*height/3 -height/6), (width, (row + 1)*height/3 - height/6 ), 4)
            break

    #2 VERTICALLY
    for col in range(0,3):
        if ((TTT [0][col] == TTT [1][col] == TTT[2][col]) and (TTT [0][col] != None)):
            winner = TTT[0][col]
            pg.draw.line(screen, (0, 250, 20), ((col + 1)*width/3 - width/6,0), ((col + 1)*width/3 - width/6, height), 4)
            break

    #3 DIAGONALLY
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] != None):
        winner = TTT[0][0]
        pg.draw.line(screen, (250, 70, 0), (50,50), (350, 350), 4)

    if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] != None):
        winner = TTT[0][2]
        pg.draw.line(screen, (250, 70, 0), (350,50), (50, 350), 4)

    if (all([all(row) for row in TTT]) and winner is None) :
        draw = True

    draw_status()

def drawXO(row, col):
    global TTT, XO
    if row == 1:
        posx =30
    if row == 2:
        posx = width/3 + 30
    if row == 3:
        posx = width*2/3 + 30


    if col == 1:
        posy =30
    if col == 2:
        posy = height/3 + 30
    if col == 3:
        posy = height*2/3 + 30

    TTT[row -1] [col -1] = XO
    if (XO == 'x') :
        screen.blit(X_img, (posy,posx))
        XO = 'o'
    else:
        screen.blit(O_img, (posy, posx))
        XO = 'x'

    pg.display.update()

def userClick():
    # GETTING COORDINATES OF OUR MOUSE CLICK
    x, y = pg.mouse.get_pos()

    #GETTING THE COLUMN OF MOUSE CLICK(1-3)
    if (x<width/3) :
        col = 1
    elif (x<width*2/3):
        col = 2
    elif (x<width):
        col = 3
    else:
        col = None

    # GETTING THE ROW PF MOUSE CLICK
    if (y<height/3):
        row = 1
    elif (y<height*2/3):
        row = 2
    elif (y<height):
        row = 3
    else:
        row = None


    if (row and col and TTT[row -1][col -1] is None):
        global XO

        #draw the x and o on screen
        drawXO(row, col)
        check_win()

def reset_game():
    global TTT, winner, XO, draw, screen
    time.sleep(3)

    XO = 'x'
    draw = False
    game_opening()
    winner = None
    TTT = [[None]*3, [None]*3, [None]*3]
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    reset_message = XO.upper() + " 's turn"
    font = pg.font.SysFont('Arial',30)
    reset_text = font.render(reset_message, 1, (255,0,0))
    screen.blit(reset_text, (width/3, 425))
    pg.display.update()


# RUNNING OUR GAME FOREVER
game_opening()

# RUNNING THE GAME IN INFINITE LOOP
while (True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            #THE USER CLICKED, PLACE AN X or O
            userClick()
            if (winner or draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)
















