import pgtrun
import random

WIDTH = 800  # Largura em Pixels
HEIGHT = 600  # Altura em pixels

gameover = False

ship = Actor('player/spaceships/playership1_blue')
ship.x = 400
ship.y = 550

gems = []

gems_colors = ("blue","green","red", "yellow")

for i in range(4):
    gem = Actor('items/gem' + gems_colors[i])
    gem.id = i
    gem.x = random.randint(5,WIDTH - 5)
    gem.y = -20
    gem.velocidade = random.randint(1,3)
    gem.ativo = False
    gems.append(gem)


hearts = []
heartx = 30

for i in range(3):
    heart = Actor('hud/hud_heartfull')
    heart.x = heartx * (i + 1)
    heart.y = 65
    heart.scale = 0.5
    heart.ativo = True
    hearts.append(heart)


score = 0
level = 0
combo  = 0
life = 3
lastCombo = 0

background = [
    {
        "pos" : (random.randint(0,WIDTH), random.randint(0,HEIGHT)),
        "size" : random.randint(1,3)
    }
    for _ in range(100)
]

def draw():
    screen.clear()
    if gameover:
        screen.draw.text('Game Over', (360, 300), color=(255,255,255), fontsize=60)
        screen.draw.text('Final Score: ' + str(score), (360, 350), color=(255,255,255), fontsize=60)
    else:
        for star in background: 
            screen.draw.filled_circle(star["pos"], star["size"], "white")
        for gem in gems:
            if gem.id == 1:
                gem.ativo = True
                gem.velocidade = 4
            if gem.ativo: 
                gem.draw()
        ship.draw()
        for heart in hearts:
            if heart.ativo:
                heart.draw()
            
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
        screen.draw.text('Level: ' + str(level + 1), (15,30), color=(255,255,255), fontsize=30)
 


def update():
    global score, combo, level, life, gameover, lastCombo
    #INPUT DE COMANDOS
    if (keyboard.right or keyboard.d) and ship.x < WIDTH - 50:
        ship.x += + 5
    elif (keyboard.left or keyboard.a) and ship.x > 50:
        ship.x += - 5

    #PRENDE A NAVE NA TELA
    if ship.x > WIDTH - 50:
        ship.x = 50
    if ship.x < 50:
        ship.x = WIDTH - 50       

    
    #GEMA PASSA DA TELA
    for gem in gems:
        if gem.y > HEIGHT + 10 and gem.ativo:
            life -= 1
            if life == 0:
                gameover = True     
            combo = 0
            if level > 0:
                level -= 1
            hearts[life].ativo = False
            resetGem(gem) 

    #GEMA É COLETADA
    for gem in gems:
        if gem.colliderect(ship) and not gameover and gem.ativo:
            combo += 1
            score += 10    
            resetGem(gem)
    
    if combo % 3 == 0 and combo > 0 and combo > lastCombo:
        level = int(combo / 3)

    #VELOCIDADE DE QUEDA DA GEMA
    for gem in gems:
        gem.y += gem.velocidade + level

    #ATUALIZA POSIÇÃO DAS ESTRELAS
    for i in range(100):
        x , y = background[i]["pos"]
        y += 1 * background[i]["size"] + level
        if y > HEIGHT:
            y = 0
            x = random.randint(0,WIDTH)
        background[i]["pos"] = (x, y)
        
def resetGem(gem):
    gem.y = -20
    gem.x = random.randint(5,WIDTH - 5)  

pgtrun.go() # Deve ser a ultima linha