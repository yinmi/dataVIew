from random_walk import RandomWalk 
import matplotlib.pyplot as plt

while True:
    rw=RandomWalk()
    rw.fill_walk()
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_valus,rw.y_valus,c=point_numbers,cmap=plt.cm.Reds,edgecolors='none',s=15)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running=input("make another walk(y/n):")
    if(keep_running=='n'):
         break