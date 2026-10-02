import pgtrun

WIDTH = 800  # Largura em Pixels
HEIGHT = 600  # Altura em pixels

box = Rect((20, 20), (50, 50))
box2 = Rect((20, 20), (50, 50))
box3 = Rect((400,300), (50, 50))

def draw():
    screen.clear()
    screen.draw.filled_rect(box, "red")
    screen.draw.filled_rect(box2, "yellow")
    screen.draw.filled_rect(box3, "blue")


def update():
    box.x = box.x + 4
    if box.x > WIDTH:
        box.x = 0
    box.y = box.y + 4
    if box.y > HEIGHT:
        box.y = 0
    box2.x = box2.x - 4
    if box2.x < 0:
        box2.x = WIDTH
    box2.y = box2.y - 4
    if box2.y < 0:
        box2.y = HEIGHT
    


pgtrun.go() # Deve ser a ultima linha