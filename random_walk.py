from random import choice
class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.x_valus=[0]
        self.y_valus=[0]

    def fill_walk(self):

        while len(self.x_valus)<self.num_points:
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance
         
            y_direction=choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance

            if x_step==0 and y_step==0:
                continue
            next_x=self.x_valus[-1]+x_step
            next_y=self.y_valus[-1]+y_step
            self.x_valus.append(next_x)
            self.y_valus.append(next_y)

