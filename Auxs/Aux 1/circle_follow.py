from pyglet.window import Window, key, mouse
from pyglet.shapes import Circle, Rectangle
from pyglet.app import run

# (0, 0) = esquina inferior izquierda de la ventana
window = Window() #con tamaño predeterminado

circle = Circle(x=window.width//2, y=window.height//2, radius=100, color=(20, 225, 30))

@window.event
def on_draw():
    window.clear()
    circle.draw()

def update_circle(x, y, dx, dy):
    circle.x, circle.y = x, y
window.on_mouse_motion = update_circle

run()
