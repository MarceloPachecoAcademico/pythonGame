import pgtrun
import random

WIDTH = 800
HEIGHT = 600

score = 0
vel = 4
game_over = False
estrelas = []
for i in range(100):
    estrela = {}
    estrela["pos"] = [[random.randint(20, 780), random.randint(20, 580)]]
    estrela["tam"] = [random.randint(1, 3)]
    estrelas.append(estrela)

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = -10


def draw(): 
    screen.clear()
    for estrela in estrelas:
        screen.draw.filled_circle(estrela["pos"], estrela["tam"], "white")
    if game_over:
        screen.draw.text('Game Over', (360, 300), color=(255,255,255), fontsize=60)
        screen.draw.text('Final Score: ' + str(score), (360, 350), color=(255,255,255), fontsize=60)
    else:
        gem.draw()
        ship.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
    ship.draw()
    gem.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)


def update():
    global score, vel, game_over
    #movimento da nave
    if (keyboard.left or keyboard.A) and ship.x > 30:
        ship.x = ship.x - 5
    if (keyboard.right or keyboard.D) and ship.x < WIDTH - 30:
        ship.x = ship.x + 5
    #movimento da gema
    gem.y += vel
    if gem.y > HEIGHT + 10:
        game_over = True
    
    if gem.colliderect(ship):
        gem.y = -10
        gem.x = random.randint(20, 780)
        score += 10
        if score % 50 == 0:
            vel += 1

pgtrun.go() # Deve ser a ultima linha
