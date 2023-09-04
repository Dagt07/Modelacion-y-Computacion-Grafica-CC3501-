import pyglet
import numpy as np


window = pyglet.window.Window(800, 600,"hola",resizable=True)
batch = pyglet.graphics.Batch()

road = pyglet.shapes.Rectangle(x=10, y=10, width=window.width-20,
                                 height=window.height-20, color=(80, 80, 80),
                                 batch=batch)

dirt = pyglet.shapes.Rectangle(x=120, y=120, width=window.width-240,
                                 height=window.height-240, color=(53, 40, 30),
                                 batch=batch)

class Car:
    def __init__(self):
        self.body = pyglet.shapes.Star(x=70, y=70, outer_radius=60, inner_radius=35,
                                       rotation=270, num_spikes=3,
                                       color=(190, 33, 78), batch=batch)
        self.advance = 0
        self.rotate = 0

        self.rotation_speed = np.pi
        self.movement_speed = 2
        self.vx = 1
        self.vy = 1

    def udpate(self):
        self.body.rotation += self.rotation_speed * self.rotate
        self.body.x += self.vx * self.advance*self.movement_speed * np.cos(np.deg2rad(self.body.rotation))
        self.body.y += self.vy * self.advance*self.movement_speed * -np.sin(np.deg2rad(self.body.rotation))
        pass

car = Car()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.W:
        car.advance = 1
    elif symbol == pyglet.window.key.S:
        car.advance = -1
    elif symbol == pyglet.window.key.A:
        car.rotate = -1
    elif symbol == pyglet.window.key.D:
        car.rotate = 1

@window.event
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.W:
        car.advance = 0
    elif symbol == pyglet.window.key.S:
        car.advance = 0
    elif symbol == pyglet.window.key.A:
        car.rotate = 0
    elif symbol == pyglet.window.key.D:
        car.rotate = 0

@window.event
def on_draw():
    window.clear()

    car.udpate()

    batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
