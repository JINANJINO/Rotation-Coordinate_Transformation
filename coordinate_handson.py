
import numpy as np
import matplotlib.pyplot as plt

##############################################
# Coordinate-Transformation
##############################################
def redraw():
    global theta_v, tx_v, ty_v

    point1 = [(square_world[0][0]-tx_v)*np.cos(theta_v) + (square_world[0][1]-ty_v)*np.sin(theta_v),
              (square_world[0][0]-tx_v)*-np.sin(theta_v) + (square_world[0][1]-ty_v)*np.cos(theta_v)]
    point2 = [(square_world[1][0]-tx_v)*np.cos(theta_v) + (square_world[1][1]-ty_v)*np.sin(theta_v),
              (square_world[1][0]-tx_v)*-np.sin(theta_v) + (square_world[1][1]-ty_v)*np.cos(theta_v)]
    point3 = [(square_world[2][0]-tx_v)*np.cos(theta_v) + (square_world[2][1]-ty_v)*np.sin(theta_v) ,
              (square_world[2][0]-tx_v)*-np.sin(theta_v) + (square_world[2][1]-ty_v)*np.cos(theta_v)]
    point4 = [(square_world[3][0]-tx_v)*np.cos(theta_v) + (square_world[3][1]-ty_v)*np.sin(theta_v),
              (square_world[3][0]-tx_v)*-np.sin(theta_v) + (square_world[3][1]-ty_v)*np.cos(theta_v) ]

    Pw =  [point1, point2, point3, point4]

    P = np.vstack([Pw, Pw[0]])  # close poly
    poly.set_data(P[:,0], P[:,1])
    title.set_text(f"viewer theta={np.degrees(theta_v):.1f}°  t=({tx_v:.2f},{ty_v:.2f})")
    plt.draw()
    

##############################################
# Scene setup
##############################################
square_world = np.array([[-0.5, -0.5],
                         [ 0.5, -0.5],
                         [ 0.5,  0.5],
                         [-0.5,  0.5]], dtype=float)


# Object pose in world
theta_v = 0.0
tx_v, ty_v = 0.0, 0.0

fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid(True)

poly, = ax.plot([], [], marker='o')
title = ax.set_title("")

help_text = (
    "PASSIVE (Viewer/Frame moves)\n"
    "[Arrows] move viewer, [W/E] rotate viewer ccw/cw\n"
    "[R] reset, [H] help toggle"
)
help_box = ax.text(0.02, 0.02, help_text, transform=ax.transAxes, va='bottom')
show_help = True


##############################################
# control
##############################################
def on_key(event):
    global theta_v, tx_v, ty_v, show_help
    step_t = 0.2
    step_r = np.radians(5.0)
    if event.key == 'left':
        tx_v -= step_t
    elif event.key == 'right':
        tx_v += step_t
    elif event.key == 'up':
        ty_v += step_t
    elif event.key == 'down':
        ty_v -= step_t
    elif event.key == 'w':
        theta_v += step_r
    elif event.key == 'e':
        theta_v -= step_r
    elif event.key == 'r':
        theta_v = 0.0; tx_v = 0.0; ty_v = 0.0
    elif event.key == 'h':
        show_help = not show_help
        help_box.set_visible(show_help)
    redraw()

fig.canvas.mpl_connect('key_press_event', on_key)
redraw()
plt.show()
