import datetime
import turtle

import pid
import sc
from const import(
    WIN_W,
    WIN_H,
    KP,
    KI,
    KD,
)

class Simulator(object):
    def __init__(self):
        self.Window = turtle.Screen()
        self.Window.setup(width=WIN_W+2, height=WIN_H+12)
        self.Window.screensize(WIN_W, WIN_H+10, "#202020")
        self.Window.setworldcoordinates(0, -10, WIN_W-1, WIN_H-1)
        self.Window.bgcolor("#202020")		# #RRGGBB in hex
        self.Window.title("Apollo-11 LM /Eagle-APS/ PID simulator !")
        
        self.Ground = turtle.Turtle()
        self.Ground.hideturtle()
        self.Ground.speed("fastest")
        self.Ground.pencolor("white")
        self.Ground.penup()
        self.Ground.goto(0, 0)
        self.Ground.pendown()
        self.Ground.goto(WIN_W - 1, 0)
     
        self.Writer = turtle.Turtle()
        self.Writer.hideturtle()
        self.Writer.speed("fastest")
        self.Writer.pencolor("white")
        self.Writer.penup()
        self.Writer.goto(0, WIN_H - 20)
        self.Writer.pendown()
        
        self.Marker = turtle.Turtle()
        self.Marker.speed("fastest")
        self.Marker.penup()
        self.Marker.left(180)
        self.Marker.color("blue")
        
        self.canvas = turtle.getcanvas()

        self.eagle = sc.SpaceCraft()
        self.pid = pid.PID(KP, KI, KD)

        self.t_sec = 0
        self.dt = datetime.datetime.now()
    
    def loop(self):
        self.Writer.write("height: {} m. (1 pix = 1 m)".format(WIN_H), move=False, align="left", font=("Arial", 10, "normal"))

        while(True):
            setpoint_abs = WIN_H - self.canvas.winfo_pointery() + self.canvas.winfo_rooty()
            setpoint = max(min(setpoint_abs, WIN_H), 0)
            self.Marker.goto(WIN_W / 2 + 35, setpoint)
            
            dt_now = datetime.datetime.now()
            t_sec_delta = (dt_now - self.dt).total_seconds()
            self.dt = dt_now
            
            power_percent = self.pid.copmpute(self.eagle.get_y(), setpoint, t_sec_delta)
            
            self.eagle.set_ddy(power_percent, t_sec_delta)
            self.eagle.set_dy(t_sec_delta)

            if power_percent > 0:
                show_flame = int(self.t_sec * 100) % 2
            else:
                show_flame = 0
            
            self.eagle.set_y(show_flame, t_sec_delta)

            print("t: {0:6.2f}, ddy: {1:6.2f}, dy: {2:6.2f}, y: {3:6.2f}, sp: {4:d}, mp: {5:6.2f}, pow: {6:6.2f}, P: {7:6.2f}, I: {8:6.2f}, D: {9:6.2f}".format(
                    self.t_sec,
                    self.eagle.get_ddy(),
                    self.eagle.get_dy(),
                    self.eagle.get_y(),
                    setpoint,
                    self.eagle.get_mp(),
                    power_percent,
                    self.pid.get_pp(),
                    self.pid.get_pi(),
                    self.pid.get_pd(),
            ))
            
            self.t_sec += t_sec_delta

                
            





