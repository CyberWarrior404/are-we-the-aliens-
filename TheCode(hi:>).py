import pgzrun
import random

WIDTH = 750
HEIGHT = 500

planet = Actor("planet.png")
planet.x = 325
planet.y  = 250
msg = "SHOOT THE ENEMY"

def draw():
    screen.fill("black")
    planet.draw()
    screen.draw.text(msg,(350,450))


def on_mouse_down(pos):
    global msg
    if planet.collidepoint(pos):
        planet.x = random.randint(50,WIDTH-50)
        planet.y = random.randint(50,HEIGHT-50)
        msg="Noice"
    else:
        msg="ARE YOU BLIND???"
    


pgzrun.go()