import pgtrun

WIDTH = 800  # Largura em Pixels
HEIGHT = 600  # Altura em pixels

dino = Actor('dino/idle1')
dino.x = 0
dino.y = 50
dino.anim.add("run", 0.66)
dino.anim.add("idle", 1.0)

background = Actor('background/grass')

def draw():
    screen.clear()
    background.draw()
    dino.draw()


def update():
    if keyboard.right or keyboard.d:
        dino.flip_x = False
        dino.x += + 5
        dino.anim.play("run")
    elif keyboard.left or keyboard.a:
        dino.flip_x = True
        dino.x += - 5
        dino.anim.play("run")
    else:
        dino.anim.play("idle")
    if keyboard.up or keyboard.w:
        dino.y += - 5
    elif keyboard.down or keyboard.s:
        dino.y += + 5

    if dino.y > HEIGHT - 50:
        dino.y = 50
    if dino.y < 50:
        dino.y = HEIGHT - 50     
    if dino.x > WIDTH - 50:
        dino.x = 50
    if dino.x < 50:
        dino.x = WIDTH - 50       


pgtrun.go() # Deve ser a ultima linha