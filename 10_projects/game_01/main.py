from turtle import Screen
from ship import Ship
from obstacles import Obstacle  # Puedes dejarlo aunque no se use todavía
from ship import Missil       # Asegúrate de importar tu clase Missil
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

ship = Ship()
obst = Obstacle()

missiles = []  # Lista para guardar todos los misiles activos

# Función para disparar un misil
def fire_missile():
    new_missile = ship.fire()
    missiles.append(new_missile)

# Teclado
screen.listen()
screen.onkey(ship.move_left, 'Left')
screen.onkey(ship.move_right, 'Right')
screen.onkey(fire_missile, 'space')

# Bucle principal
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    
    # Mover todos los misiles
    for missile in missiles:
        missile.move()
