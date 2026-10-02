import pgtrun

WIDTH = 800  # Largura em Pixels
HEIGHT = 600  # Altura em pixels

ator = Actor('idle1')
ator.x = 100
ator.y = 100
dir = 5
background = Actor('sand')
ator.anim.add("run", 1.5)

def draw():
    screen.clear()
    background.draw()
    ator.draw()
    


def update():
    ator.anim.play("run")
    global dir
    ator.x += dir
    if ator.x > WIDTH - 100:
        dir *= -1
        ator.flip_x = True
    if ator.x < 100:
        dir *= -1
        ator.flip_x = False

pgtrun.go() # Deve ser a ultima linha
