import random as r

def RandomWalk(x0, y0, t0, L, tau, s, runs, seed):
    # Where x_0, y_0 are the initial spatial coordinates
    #       t_0 is the initial time
    #       L is the spacial step length (km)
    #       tau is the temporal step length (days)
    #       steps is the total number of steps or stopping probability
    #       runs is the number of simulations 
    #       seed is the random number seed for reproducibility 
  
    r.seed(seed)
  
    if s < 1 :
        sprob = s
    elif s > 1 :
        steps = s
    else : 
        raise Exception("This is only one step!")
        
    #initiallizes coordinate vectors
    runsbysteps <- array(dim=c(steps,3,runs))
  
  runsbysteps[1,,] <- c(x_0,y_0,t_0)
  
  #Runs any number of simmulations 
  for (i in 1:runs)
  {
    #Computes position at each time step
    for (j in 2:steps)
    {
      #theta is the direction of movement (from a uniform random distribution)
      #0 is East
      theta <- runif(1, 0, 2*pi)
      
      #displacement in this step
      dx <- L * cos(theta)
      dy <- L * sin(theta)
    
      runsbysteps[j,,i]<-runsbysteps[j-1,,i]+c(dx,dy,tau)
    }
  }
  
  if (runs!=1)
    {
    results<-runsbysteps[steps,,]
    } else{
    results<-runsbysteps[,,1]
    }
  
  return(results)
}

SingleRun <- function(x_0, y_0, t_0, L, tau, steps, seed)
{
  coords <- RandomWalk(x_0, y_0, t_0, 1, 1, steps, 1, seed)
  lim <- c(-1.25*max(abs(coords[,1:2])),1.25*max(abs(coords[,1:2])))
  plot( coords[,1],coords[,2],type='l',bty='n',xaxt='n',yaxt='n',
        xlab='x coordinate', ylab='y coordinate',
        xlim=lim, ylim=lim)
  axis(1, pos=0, col = "lightgrey")
  axis(2, pos=0, col="lightgrey", las=1)
}

MultiRun <- function(x_0, y_0, t_0, L, tau, steps, runs, seed)
{
  results <- RandomWalk(x_0, y_0, t_0, L, tau, steps, runs, seed)
  lim <- c(-1.25*max(abs(results[1:2,])),1.25*max(abs(results[1:2,])))
  plot( results[1,],results[2,],type='p',bty='n',xaxt='n',yaxt='n',
        xlab='x coordinate', ylab='y coordinate',
        xlim=lim, ylim=lim)
  axis(1, pos=0, col = "lightgrey")
  axis(2, pos=0, col="lightgrey", las=1)
  symbols(x_0, y_0, circles=5, add=T)
}
  
MultiRun(0,0,0,1,1,100,100,666)


