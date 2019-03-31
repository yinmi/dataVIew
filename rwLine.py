from random_walk import RandomWalk 
import matplotlib.pyplot as plt

rw=RandomWalk()
rw.fill_walk()
point_numbers=list(range(rw.num_points))
plt.plot(rw.x_valus,rw.y_valus,linewidth=1)
plt.show()