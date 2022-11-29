######################################################################################################################
# Name: Cameron White
# Date:10/26/22
# Description: Chaos game with multiple diffrent shapes
######################################################################################################################
from tkinter import *
from random import choice
from FRACTAL_DESIGN_TEAM import *

# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520

# the implemented fractals
FRACTALS = [ "SierpinskiTriangle", "SierpinskiCarpet", "Pentagon", "Hexagon", "Octagon" ]

class ChaosGame(Canvas):
    def __init__(self,parent):
        
        super().__init__(parent,width = WIDTH, height = HEIGHT, bg= 'white')
        #defines dimension dictionary which includes max,min,and mid values of points and all other properties of the game
        self.dimensions = {'vertex_radius':2, 'vertex_color':'red', 'point_color':'black', 'point_radius':0, 'min_x':5,'min_y':5}
        self.dimensions['max_x']= WIDTH - 5
        self.dimensions['max_y']= HEIGHT - 5
        self.dimensions['mid_y']= (self.dimensions['min_y'] + self.dimensions['max_y'])/2
        self.dimensions['mid_x']= (self.dimensions['min_x'] + self.dimensions['max_x'])/2
        self.pack()
        
    def make(self,shape):
        if shape == "SierpinskiTriangle":
            
            shape = SierpinskiTriangle(self.dimensions)
            self.plot_point(shape.v1,'red',1)
            self.plot_point(shape.v2,'red',1)
            self.plot_point(shape.v3,'red',1)
            #first _point
            nu_point = shape.v2.midpt(shape.v3)
            # make points based off number of points needed to make shape
            for i in range(shape.num_points + 1):
                #new point
                self.plot_point(nu_point,self.dimensions['point_color'], self.dimensions['point_radius'])
                #picks from random vertex
                nu_point = nu_point.midpt(choice([shape.v1,shape.v2,shape.v3]))
                
        if shape == "SierpinskiCarpet":
            
            shape = SierpinskiCarpet(self.dimensions)
            self.plot_point(shape.v1,'blue',1)
            self.plot_point(shape.v2,'blue',1)
            self.plot_point(shape.v3,'blue',1)
            self.plot_point(shape.v4,'blue',1)
            self.plot_point(shape.v5,'blue',1)
            self.plot_point(shape.v6,'blue',1)
            self.plot_point(shape.v7,'blue',1)
            self.plot_point(shape.v8,'blue',1)
            #first _point
            nu_point = shape.v2.interpt((shape.v3),shape.r)
            # make points based off number of points needed to make shape
            for i in range(shape.num_points + 1):
                #new point
                self.plot_point(nu_point,self.dimensions['point_color'], self.dimensions['point_radius'])
                #picks random vertex and plots point 0.8 away from og point
                nu_point = nu_point.interpt(choice([shape.v1,shape.v2,shape.v3,shape.v4,shape.v5,shape.v6,shape.v7,shape.v8]),shape.r)
            
        if shape == "Pentagon":
            shape = Pentagon(self.dimensions)
            self.plot_point(shape.v1,'medium violet red',1)
            self.plot_point(shape.v2,'medium violet red',1)
            self.plot_point(shape.v3,'medium violet red',1)
            self.plot_point(shape.v4,'medium violet red',1)
            self.plot_point(shape.v5,'medium violet red',1)
            
            #first _point
            nu_point = shape.v2.interpt((shape.v3),shape.r)
            # make points based off number of points needed to make shape
            for i in range(shape.num_points + 1):
                
                #new point
                self.plot_point(nu_point,self.dimensions['point_color'], self.dimensions['point_radius'])
                #picks random vertex and plots point 0.8 away from og point
                nu_point = nu_point.interpt(choice([shape.v1,shape.v2,shape.v3,shape.v4,shape.v5]),shape.r)

        if shape == "Hexagon":
            shape = Hexagon(self.dimensions)
            self.plot_point(shape.v1,'cyan',1)
            self.plot_point(shape.v2,'cyan',1)
            self.plot_point(shape.v3,'cyan',1)
            self.plot_point(shape.v4,'cyan',1)
            self.plot_point(shape.v5,'cyan',1)
            self.plot_point(shape.v6,'cyan',1)

            #first _point
            nu_point = shape.v2.interpt((shape.v3),shape.r)
            # make points based off number of points needed to make shape
            for i in range(shape.num_points + 1):
                
                #new point
                self.plot_point(nu_point,self.dimensions['point_color'], self.dimensions['point_radius'])
                #picks random vertex and plots point 0.8 away from og point
                nu_point = nu_point.interpt(choice([shape.v1,shape.v2,shape.v3,shape.v4,shape.v5,shape.v6]),shape.r)
                
        if shape == "Octagon":
           
            shape = Octagon(self.dimensions)
            self.plot_point(shape.v1,'yellow',1)
            self.plot_point(shape.v2,'yellow',1)
            self.plot_point(shape.v3,'yellow',1)
            self.plot_point(shape.v4,'yellow',1)
            self.plot_point(shape.v5,'yellow',1)
            self.plot_point(shape.v6,'yellow',1)
            self.plot_point(shape.v7,'yellow',1)
            self.plot_point(shape.v8,'yellow',1)

            #first _point
            nu_point = shape.v2.interpt((shape.v3),shape.r)
            # make points based off number of points needed to make shape
            for i in range(shape.num_points + 1):
                
                #new point
                self.plot_point(nu_point,self.dimensions['point_color'], self.dimensions['point_radius'])
                #picks random vertex and plots point 0.8 away from og point
                nu_point = nu_point.interpt(choice([shape.v1,shape.v2,shape.v3,shape.v4,shape.v5,shape.v6,shape.v7,shape.v8]),shape.r)


    def plot_point(self,point, color , radius):

        #plots point on canvas
        self.create_oval(point.x-radius*2, point.y - radius*2 , point.x + radius*2 , point.y + radius*2, outline = color, fill = color)

# create the fractals in individual (sequential) windows
for f in FRACTALS:
    window = Tk()
    window.geometry("{}x{}".format(WIDTH, HEIGHT))
    window.title("The Chaos Game...Reloaded")
    # create the game as a Tkinter canvas inside the window
    s = ChaosGame(window)
    # make the current fractal
    s.make(f)
    # wait for the window to close
    window.mainloop()

