
import numpy as np
import matplotlib.pyplot as plt

##############################################
# translation & rotation calculate
##############################################

def redraw():
    global theta, tx, ty

    point1 = [square_local[0][0]*np.cos(theta) - square_local[0][1]*np.sin(theta) + tx,
              square_local[0][0]*np.sin(theta) + square_local[0][1]*np.cos(theta) + ty]
    point2 = [square_local[1][0]*np.cos(theta) - square_local[1][1]*np.sin(theta) + tx,
              square_local[1][0]*np.sin(theta) + square_local[1][1]*np.cos(theta) + ty]
    point3 = [square_local[2][0]*np.cos(theta) - square_local[2][1]*np.sin(theta) + tx,
              square_local[2][0]*np.sin(theta) + square_local[2][1]*np.cos(theta) + ty]
    point4 = [square_local[3][0]*np.cos(theta) - square_local[3][1]*np.sin(theta) + tx,
              square_local[3][0]*np.sin(theta) + square_local[3][1]*np.cos(theta) + ty]

    Pw = [point1, point2, point3, point4]

    P = np.vstack([Pw, Pw[0]])  # close poly
    poly.set_data(P[:,0], P[:,1])
    title.set_text(f"theta={np.degrees(theta):.1f} deg  t=({tx:.2f},{ty:.2f})")
    plt.draw()

##############################################
# Scene setup
##############################################
square_local = np.array([[-0.5, -0.5],
                         [ 0.5, -0.5],
                         [ 0.5,  0.5],
                         [-0.5,  0.5]], dtype=float)

# Object pose in world
theta = 0.0
tx, ty = 0.0, 0.0

fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid(True)

poly, = ax.plot([], [], marker='o')
title = ax.set_title("")

help_text = (
    "ACTIVE (Object moves)\n"
    "[Arrows] translate, [W/E] rotate ccw/cw\n"
    "[R] reset, [H] help toggle"
)
help_box = ax.text(0.02, 0.02, help_text, transform=ax.transAxes, va='bottom')

show_help = True


##############################################
# control
##############################################
def on_key(event):
    global theta, tx, ty, show_help
    step_t = 0.2
    step_r = np.radians(5.0)
    if event.key == 'left':
        tx -= step_t
    elif event.key == 'right':
        tx += step_t
    elif event.key == 'up':
        ty += step_t
    elif event.key == 'down':
        ty -= step_t
    elif event.key == 'w':
        theta += step_r
    elif event.key == 'e':
        theta -= step_r
    elif event.key == 'r':
        theta = 0.0; tx = 0.0; ty = 0.0
    elif event.key == 'h':
        show_help = not show_help
        help_box.set_visible(show_help)
    redraw()

fig.canvas.mpl_connect('key_press_event', on_key)
redraw()
plt.show()
