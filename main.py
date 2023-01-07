import random
import pgzrun

WIDTH = 800
HEIGHT = 600

sun = Actor("sun.png")
sun.timer = 0
sun.points = 0

def draw():
    screen.fill("skyblue")
    sun.draw()
    screen.draw.text(text="Suma punktów: " + str(sun.points), center = (WIDTH / 2, 30), color = "black", fontsize = 50)

def update():
    sun.timer -= 1

    if sun.timer <= 0:
        sun.x = random.randint(80, WIDTH - 80)
        sun.y = random.randint(80, HEIGHT - 80)
        sun.timer = 60 - sun.points

def on_mouse_down(pos):
    if sun.collidepoint(pos):
        sun.points += 1
        sun.timer = 0
    else:
        sun.points -= 1
        sun.timer = 0

pgzrun.go()



