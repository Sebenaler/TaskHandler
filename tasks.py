#script to check all task that I have to do
#going to use pygame for my GUI 
import pygame as py

py.init()
screen = py.display.set_mode((1280,720))
clock = py.time.Clock()
running = True

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
#need to add 4 clickable rectangles
 #  -top left current tasks
 #  -bottom left calendar 
 #  -top right complete tasks
 #  -bottom right do not know yet

    screen.fill((173,216,230))
    py.draw.rect(screen,(0,0,139),py.Rect(10,10,625,345))
    py.draw.rect(screen,(0,139,0),py.Rect(645,10,625,345))
    py.draw.rect(screen,(139,0,0),py.Rect(10,370,625,340))
    py.draw.rect(screen,(255,255,104),py.Rect(645,370,625,340))
    py.display.flip()
    clock.tick(30)
py.quit()