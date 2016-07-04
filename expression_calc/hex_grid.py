import numpy as np
import pylab as plt

class Hgrid():

    def __init__(self):
        pass

    def hex_grid(self,hex_dim,l):
        side = hex_dim + 1
        ant_main_row = side + hex_dim
        
        elements = 1

        #summing the antennas in hexactoganal rings 
        for k in xrange(hex_dim):
            elements = elements + (k+1)*6
                
        ant_x = np.zeros((elements,),dtype=float)
        ant_y = np.zeros((elements,),dtype=float)
        print "len(ant_x) = ",len(ant_x)
        print "len(ant_y) = ",len(ant_y)
        x = 0.0
        y = 0.0

        counter = 0
        
        for k in xrange(side):
            x_row = x
            y_row = y
            for i in xrange(ant_main_row):
                if k == 0:
                   ant_x[counter] = x_row 
                   ant_y[counter] = y_row
                   x_row = x_row + l
                   counter = counter + 1 
                else:
                   ant_x[counter] = x_row
                   ant_y[counter] = y_row
                   counter = counter + 1
                   
                   ant_x[counter] = x_row
                   ant_y[counter] = -1*y_row
                   x_row = x_row + l
                   counter = counter + 1   
            x = x + l/2.0
            y = y + (np.sqrt(3)/2.0)*l                 
            ant_main_row = ant_main_row - 1
    
        return ant_x,ant_y

    def calculate_phi(self,ant_x,ant_y):
        for k in xrange(len(ant_x)):
            for j in xrnage(k+1,len(ant_x)) 
 


if __name__ == "__main__":
   h = Hgrid()
   ant_x,ant_y = h.hex_grid(4,20)
   plt.plot(ant_x,ant_y,"ro")
   plt.show()
   print "Hallo"

