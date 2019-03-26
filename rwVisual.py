from random_walk import RandomWalk 
import matplotlib.pyplot as plt

while True:
    rw=RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_valus,rw.y_valus,s=15)
    plt.show()

    keep_running=input("make another walk(y/n):")
    if(keep_running=='n'):
         break