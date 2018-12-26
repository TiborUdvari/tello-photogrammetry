import math
import pyglet
import numpy as np
import pyglet
from pyglet.gl import *
from pyglet.window import *
from math import *

win = pyglet.window.Window()

frame = 0
def update_frame(x, y):
    global frame
    frame += 1

def makeCircle(numPoints, r):
    verts = []
    for i in range(numPoints):
        angle = radians(float(i)/numPoints * 360.0)
        x = r*cos(angle)
        y = r*sin(angle)
        verts += [x,y]
    global circle
    return pyglet.graphics.vertex_list(numPoints, ('v2f', verts))

circle = makeCircle(200, 100)

@win.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glLoadIdentity()

    # translate into the middle
    w, h = win.get_size()

    glPushMatrix()
    glTranslatef(w/2, h/2, 0)

    #glTranslatef(w / 2, 1, 0, 0)
    #glRotatef(frame / 100.0, 0.0, 0.0, 1.0)

    glBegin(GL_TRIANGLES)
    glVertex3f(0,10,0)
    glVertex3f(10,-10,0)
    glVertex3f(-10,-10,0)
    glEnd()
    circle.draw(GL_LINE_LOOP)

    glPopMatrix()


pyglet.clock.schedule(update_frame, 1/10.0)
pyglet.app.run()