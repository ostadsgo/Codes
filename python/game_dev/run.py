WIDTH = 600
HEIGHT = 400
# colors
WHITE = (255, 255, 255)
alien = Actor("alien.webp")
alien.pos = 100, 56


def draw():
    screen.clear()
    screen.fill(WHITE)
    alien.draw()

steps = 10
def update():
    global steps
    alien.x += steps 
    if alien.right >= WIDTH:
        steps = -10
    if alien.left <= 0:
        steps += 10
        

