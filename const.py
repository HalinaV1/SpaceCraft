WIN_W = 400
WIN_H = 700

INIT_X = WIN_W / 2
INIT_Y = 0              # m
INIT_DY = 0             # m/s

GRAVITY = -1.62         # 1.62 m/s^2 (The Moon)

# Characteristics and parameters were taken from:
# https://en.m.wikipedia.org/wiki/Apollo_Lunar_Module
MASS_DRY = 2300         # kg
MASS_PROPELLANT = 2400  # kg
MAX_THRUST = 16000      # N
TSFC = 300              # g/kN*s

KP = 13
KI = 0.5
KD = 100
