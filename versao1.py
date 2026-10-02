import pgtrun

WIDTH = 800
HEIGHT = 600
TITLE = "Semaforo"

def draw():
    screen.clear()
    screen.draw.circle((250, 250), 50, "white")
    screen.draw.filled_circle((250, 100), 50, "red")
    screen.draw.line((150, 20), (150, 500), "purple")
    screen.draw.line((150, 20), (350, 20), "purple")
    screen.draw.filled_circle((250, 400), 50, "green")
    screen.draw.line((150, 500), (350, 500), "purple")
    screen.draw.line((350, 20), (350,500), "purple")

    screen.draw.circle((500, 250), 20, "white")
    screen.draw.line((500, 270), (500, 320), "white")
    screen.draw.line((500, 320), (515, 335), "white")
    screen.draw.line((500, 320), (485, 335), "white")
    screen.draw.line((480, 280), (520,280), "white")


pgtrun.go() 