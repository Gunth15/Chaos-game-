from tkinter import *
from random import randint
from math import cos,sin, pi
class Fractal():
    def __init__(self,dimensions):
        #canvas dimensions
        self.dimensions = dimensions
        
        #the default number of plots to plot
        self.num_points = 50000
        
        # the default distance ratio is halfway
        self.r = 0.5

    def frac_x(self,r):
        #returns x between dimension resrictions default to midpoint x
        return int((self.dimensions["max_x"] - self.dimensions["min_x"]) * r) + self.dimensions["min_x"]


    def frac_y(self,r):
        #returns y between dimension resrictions default to midpoint y
        return int((self.dimensions["max_y"] - self.dimensions["min_y"]) * r) + self.dimensions["min_y"]

#implemented from previus chaos game iterations   
class Point():

    # write your code for the point class here (and subsequently remove this comment)
    def __init__(self, x = 0, y = 0):
        
            #GET name and position of x an y value that makepup the point
            self.x = x
            self.y = y
                
    def dist(self,o_point):
    #Determine distance from current point to selceted point(other_point) and thereturn it
        
            #Use distance formula to calculate distance(duh!!), return value
            return (((o_point.x - self.x)**2) + ((o_point.y - self.y)**2))**(1/2)
        
    def __str__(self):
            #returns the x and y coardinates of the points in appropriate format
            return "({},{})".format(self.x,self.y)
        
    #Finds point between initiate point and selected point
    def midpt(self,o_point):
                
            # returns midpoint using formula [x + x2]/2 and [y + y2]/2
            mx = (self.x + o_point.x)/2
            my = (self.y + o_point.y)/2
            return Point(mx, my)
        
    @property
    def x(self):
            return self._x
    @x.setter
    def x(self,val):
            self._x = val
                
    @property
    def y(self):
            return self._y
    @y.setter
    def y(self,val):
            self._y = val
            
    def interpt(self, other, r):
        # make sure that the distance ratio is expressed from a
        # smaller component value to a larger one
        # first, the x-component
        rx = r
        if (self.x > other.x):
            rx = 1.0 - r
        # next, the y-component
        ry = r
        if (self.y > other.y):
            ry = 1.0 - r
            
        # calculate the new point's coordinates
        # the difference in the components (distance between the
        # points) is first scaled by the specified distance ratio
        # the minimum of the components is then added back in order
        # to obtain the coordinates in between the two points (and
        # not with respect to the origin)
        x = abs(self.x - other.x) * rx + min(self.x, other.x)
        y = abs(self.y - other.y) * ry + min(self.y, other.y)

        return Point(x, y)
   
class SierpinskiTriangle(Fractal):
    def __init__(self,dimensions):
        #fractal inheritance
        super().__init__(dimensions)
        
        #vertices
        self.v1 = Point(dimensions['mid_x'],dimensions['min_y'])
        self.v2 = Point(dimensions['min_x'],dimensions['max_y'])
        self.v3 = Point(dimensions['max_x'],dimensions['max_y'])
        
class SierpinskiCarpet(Fractal):

    def __init__(self,dimensions):
        #fractal inheritance
        super().__init__(dimensions)
        # new amnt of points needed to genreate 100000
        self.num_points = 100000
        #new ratio
        self.r  = 0.66
        #Vertices
        self.v1 = Point(dimensions['min_x'],dimensions['min_y'])
        self.v2 = Point(dimensions['mid_x'],dimensions['min_y'])
        self.v3 = Point(dimensions['max_x'],dimensions['min_y'])
        self.v4 = Point(dimensions['min_x'],dimensions['mid_y'])
        self.v5 = Point(dimensions['max_x'],dimensions['mid_y'])
        self.v6 = Point(dimensions['min_x'],dimensions['max_y'])
        self.v7 = Point(dimensions['mid_x'],dimensions['max_y'])
        self.v8 = Point(dimensions['max_x'],dimensions['max_y'])
    
class Pentagon(Fractal):
    
        def __init__(self,dimensions):
            #fractal inheritance
            super().__init__(dimensions)
            #new ratio
            self.r  = 0.618
            #Vertices
            self.v1 = Point(dimensions['mid_x'] + dimensions['mid_x']*cos(2*pi/5+60),(self.frac_y(0.5375) + dimensions['mid_y']*sin(2*pi/5+60)))
            self.v2 = Point(dimensions['mid_x'] + dimensions['mid_x']*cos(4*pi/5+60),(self.frac_y(0.5375) + dimensions['mid_y']*sin(4*pi/5+60)))
            self.v3 = Point(dimensions['mid_x'] + dimensions['mid_x']*cos(6*pi/5+60),(self.frac_y(0.5375) + dimensions['mid_y']*sin(6*pi/5+60)))
            self.v4 = Point(dimensions['mid_x'] + dimensions['mid_x']*cos(8*pi/5+60),(self.frac_y(0.5375) + dimensions['mid_y']*sin(8*pi/5+60)))
            self.v5 = Point(dimensions['mid_x'] + dimensions['mid_x']*cos(10*pi/5+60),(self.frac_y(0.5375) + dimensions['mid_y']*sin(10*pi/5+60)))


class Hexagon(Fractal):
     def __init__(self,dimensions):
            #fractal inheritance
            super().__init__(dimensions)
            #new ratio
            self.r  = 0.665
            #Vertices
            self.v1 = Point(dimensions['mid_x'],dimensions['min_y'])
            self.v2 = Point(dimensions['min_x'],self.frac_y(0.25))
            self.v3 = Point(dimensions['max_x'],self.frac_y(0.25))
            self.v4 = Point(dimensions['min_x'],self.frac_y(0.75))
            self.v5 = Point(dimensions['max_x'],self.frac_y(0.75))
            self.v6 = Point(dimensions['mid_x'],dimensions['max_y'])

class Octagon(Fractal):
         def __init__(self,dimensions):
            #fractal inheritance
            super().__init__(dimensions)
            # new amnt of points needed to genreate 100000
            self.num_points = 75000
            #new ratio
            self.r  = 0.705
            #Vertices
            self.v1 = Point(self.frac_x(0.2925),dimensions['min_y'])
            self.v2 = Point(self.frac_x(0.7075),dimensions['min_y'])
            self.v3 = Point(dimensions['min_x'],self.frac_y(0.2925))
            self.v4 = Point(dimensions['max_x'],self.frac_y(0.2925))
            self.v5 = Point(dimensions['min_x'],self.frac_y(0.7075))
            self.v6 = Point(dimensions['max_x'],self.frac_y(0.7075))
            self.v7 = Point(self.frac_x(0.2925),dimensions['max_y'])
            self.v8 = Point(self.frac_x(0.7075),dimensions['max_y'])

