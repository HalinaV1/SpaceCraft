import turtle

from const import (
    WIN_W,
    WIN_H,
    INIT_X,
    INIT_Y,
    INIT_DY,
    MASS_DRY,
    MASS_PROPELLANT,
    TSFC,
    MAX_THRUST,
    GRAVITY,
)

class SpaceCraft(object):
    def __init__(self):
        self.SpaceCraft = turtle.Turtle()
        self.SpaceCraft.penup()
        self.SpaceCraft.speed("fastest")
        self.SpaceCraft.shape("circle")
        self.SpaceCraft.shapesize(0.5, 2)
        self.SpaceCraft.color("#00BB00")	# #RRGGBB in hex
        self.SpaceCraft.goto(INIT_X, INIT_Y)
        
        self.Flame = turtle.Turtle()
        self.Flame.hideturtle()
        self.Flame.penup()
        self.Flame.speed("fastest")
        self.Flame.shape("circle")
        self.Flame.shapesize(1, 0.25)
        self.Flame.color("orange")
        self.Flame.goto(INIT_X, INIT_Y - 20)
        
        self.mass_dry = MASS_DRY
        self.mass_propellant = MASS_PROPELLANT
        self.ddy = 0
        self.dy = INIT_DY
        self.y = INIT_Y

    def set_ddy(self, thrust_p, tsec_delta):
        thrust_p = min(thrust_p, 100) # make sure t_p <= 100
        thrust_requested = thrust_p * MAX_THRUST / 100
        propellant_needed = TSFC * thrust_requested * tsec_delta / (1000 * 1000)
        
        if propellant_needed < self.mass_propellant:
            thrust = thrust_requested
            self.ddy = GRAVITY + (thrust / (self.mass_dry + self.mass_propellant))
            self.mass_propellant -= propellant_needed
        else:
            self.ddy = GRAVITY
            self.mass_propellant = 0
    
    def get_ddy(self):
        return self.ddy
    
    def set_dy(self, tsec_delta):
        self.dy += self.ddy * tsec_delta

    def get_dy(self):
        return self.dy

    def set_y(self, show_flame, tsec_delta):
        self.y = max(self.y + self.dy * tsec_delta, 0)
        self.SpaceCraft.sety(self.y)
        self.Flame.sety(self.y - 20)

        if show_flame and self.mass_propellant > 0:
            self.Flame.showturtle()
        else:
            self.Flame.hideturtle()

        if self.y == 0:
            self.ddy = 0
            self.dy = 0
    
    def get_y(self):
        return self.y

    def get_mp(self):
        return self.mass_propellant






