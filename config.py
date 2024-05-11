
import math
import glm

WINDOWSIZE = (1920, 1000)
FPS = 60


PLAYER_SPEED = 400

ASPECT_RATIO = WINDOWSIZE[0] / WINDOWSIZE[1]
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)  # vertical FOV
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)
NEAR = 0.1
FAR = 2000.0