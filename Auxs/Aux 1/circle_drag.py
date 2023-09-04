from pyglet.window import Window, key, mouse
from pyglet.shapes import Circle, Rectangle
from pyglet.app import run

# (0, 0) = esquina inferior izquierda de la ventana
window = Window()

circle = Circle(x=window.width//2, y=window.height//2, radius=100, color=(20, 225, 30))

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        circle.x, circle.y = x, y

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & mouse.LEFT:
        circle.x, circle.y = x, y

@window.event
def on_draw():
    window.clear()
    circle.draw()

run(1/120) #que vaya a 120hz, si se deja run() se adapta por defecto al monitor
