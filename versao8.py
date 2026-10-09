import pgtrun
import random

WIDTH = 800
HEIGHT = 600
# pontuação
score=0
# Velocidade da queda (aumenta em função da pontuação)
vel=3
# Final de jogo
game_over = False
# criando um array de estrelas (posição)

estrelas=[]
for i in range(100):
    # posição
    estrela = {}
    estrela["pos"]=[random.randint(20, 780), random.randint(20, 580)] 
    # tamanho
    estrela["tam"]=random.randint(1,5)
    estrelas.append(estrela)

# um set com os nomes dos arquivos png dos atores 
atores_img= ("items/gemblue","items/gemred", "items/gemyellow", "items/gemgreen")

# uma lista vazia de joias
gems=[]

# quantidade de chamadas ao update
chamadas_update = 0


ship = Actor('player/spaceships/playership1_blue')

ship.x = 370
ship.y = 550
# metade da largura da nave
larg = int(ship.midright[0]-ship.center[0])

def draw():
    screen.clear()
    for estrela in estrelas:
        screen.draw.filled_circle(estrela["pos"], estrela["tam"], ("white"))

    if game_over:
        screen.draw.text('Game Over', (360, 300), color=(0,255,0), fontsize=60)
        screen.draw.text('Final Score: ' + str(score), (360, 350), color=(255,255,255), fontsize=60)
    else:
        # desenhar as 4 gemas
        for joia in gems:
            joia["gem"].draw()
        
        # desenha a nave
        ship.draw()

        #desenha o placar
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)


def update():
    global score,vel,game_over,chamadas_update
    # atualizando a posição da nave
    if keyboard.left:
        ship.x = ship.x - 10
    if keyboard.right:
        ship.x = ship.x + 10
    # Impedir que a nave saia da tela
    if ship.x > WIDTH - larg:
        ship.x -= 25
    if ship.x < larg :
        ship.x += 25

    # Aplica gravidade nas 4 gema
    for joia in gems:
        joia["gem"].y += vel
        if joia["gem"].y > HEIGHT :
            if joia["pontos"] > 0:
                game_over=True
            else:
                gems.remove(joia) 

    # teste de colisão com as 4 gemas
    for joia in gems:
        if joia["gem"].colliderect(ship):
            score += joia["pontos"]
            gems.remove(joia)
            if score % 20 == 0:
                vel = vel + 1

    chamadas_update +=1
    if(len(gems)< len(atores_img) and chamadas_update%30 == 0):
        # Criar mais uma joia
        i = len(gems)
        pontos= random.randint(-2,5)
        if pontos > 0:
            gem = Actor(atores_img[i],(random.randint(20, 780),0))
        else:
            gem = Actor("dino/idle1",(random.randint(20, 780),0))    
        gems.append({"gem":gem, "pontos":pontos})
    
pgtrun.go() # Deve ser a ultima linha