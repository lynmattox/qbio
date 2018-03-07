import random as r
import numpy as n 
from operator import add 

def RandomWalk(x0, y0, t0, L, tau, s, runs, seed):
    # Where x_0, y_0 are the initial spatial coordinates
    #       t_0 is the initial time
    #       L is the spacial step length (km)
    #       tau is the temporal step length (days)
    #       steps is the total number of steps or stopping probability
    #       runs is the number of simulations 
    #       seed is the random number seed for reproducibility 
  
    r.seed(seed)
    
    sprob = 0
    steps = 0
    
    if s < 1 :
        sprob = s
    elif s > 1 :
        steps = s
    else : 
        raise Exception("This is only one step!")
        
    #initiallizes coordinate vectors, as a list of lists
    trials = []
     
    #For any number of simulations
    for i in range(0,runs-1) :
        trials[i] = []
        trials[i].append([x_0,y_0,t_0])
        
        j = 1
        stop = 0
        #Computes position at each time step
        while j < steps or stop = 0 :
    
            #theta is the direction of movement (from a uniform random distribution)
            #0 is East
            theta = r.uniform(0,2*n.pi)
      
            #displacement in this step
            dx = L * n.cos(theta)
            dy = L * n.sin(theta)
    
            trials[i].append(map(add, trials[i][j-1],[dx, dy, tau]))
            j += 1
            
            if r.uniform(0,1) < sprob
                stop = 1
            

    if runs != 1 :
        results = trials[:][-1]
     
    else :
        results = trials[0]
    
    return(results)

Walk1 = RandomWalk(0,0,0,1,1,100,1,999)
print(Walk1)

#SingleRun <- function(x_0, y_0, t_0, L, tau, steps, seed)
#{
#  coords <- RandomWalk(x_0, y_0, t_0, 1, 1, steps, 1, seed)
#  lim <- c(-1.25*max(abs(coords[,1:2])),1.25*max(abs(coords[,1:2])))
#  plot( coords[,1],coords[,2],type='l',bty='n',xaxt='n',yaxt='n',
#        xlab='x coordinate', ylab='y coordinate',
#        xlim=lim, ylim=lim)
#  axis(1, pos=0, col = "lightgrey")
#  axis(2, pos=0, col="lightgrey", las=1)
#}
#
#MultiRun <- function(x_0, y_0, t_0, L, tau, steps, runs, seed)
#{
#  results <- RandomWalk(x_0, y_0, t_0, L, tau, steps, runs, seed)
#  lim <- c(-1.25*max(abs(results[1:2,])),1.25*max(abs(results[1:2,])))
#  plot( results[1,],results[2,],type='p',bty='n',xaxt='n',yaxt='n',
#        xlab='x coordinate', ylab='y coordinate',
#        xlim=lim, ylim=lim)
#  axis(1, pos=0, col = "lightgrey")
#  axis(2, pos=0, col="lightgrey", las=1)
#  symbols(x_0, y_0, circles=5, add=T)
#}
#  
#MultiRun(0,0,0,1,1,100,100,666)


