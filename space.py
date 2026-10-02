import pgtrun
import random

WIDTH = 800  # Largura em Pixels
HEIGHT = 600  # Altura em pixels

gameover = False

ship = Actor('player/spaceships/playership1_blue')
ship.x = 400
ship.y = 550

gem = Actor('items/gemblue')
gem.x = random.randint(5,WIDTH - 5)
gem.y = -20

heart = Actor('hud/hud_heartfull')
heart.x = 30
heart.y = 65
heart.scale = 0.5

heart2 = Actor('hud/hud_heartfull')
heart2.x = 60
heart2.y = 65
heart2.scale = 0.5

heart3 = Actor('hud/hud_heartfull')
heart3.x = 90
heart3.y = 65
heart3.scale = 0.5

score = 0
level = 0
combo  = 0
life = 3

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
        gem.draw()
        ship.draw()
        if life > 0:
            heart.draw()
        if life > 1:
            heart2.draw()
        if life > 2:
            heart3.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
        screen.draw.text('Level: ' + str(level + 1), (15,30), color=(255,255,255), fontsize=30)
 


def update():
    global score, combo, level, life, gameover
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
    if gem.y > HEIGHT + 10:
        life -= 1
        if life == 0:
           gameover = True     
        combo = 0
        if level > 0:
            level -= 1
        resetGem() 

    #GEMA É COLETADA
    if gem.colliderect(ship) and not gameover:
        combo += 1
        score += 10    
        resetGem()
    
    if combo > 0:
        level = int(combo / 3)

    #VELOCIDADE DE QUEDA DA GEMA
    gem.y += 5 + level

    #ATUALIZA POSIÇÃO DAS ESTRELAS
    for i in range(100):
        x , y = background[i]["pos"]
        y += 1 + level
        if y > HEIGHT:
            y = 0
        background[i]["pos"] = (x, y)
        
 
def resetGem():
    global gem
    gem.y = -20
    gem.x = random.randint(5,WIDTH - 5)  

pgtrun.go() # Deve ser a ultima linha