from random import randint
class Die():
    """表示一个筛子的的类""" 
    def __init__(self,num_sides=6):
        """筛子默认6"""
        self.num_sides=num_sides
    def roll(self):
        return randint(1,self.num_sides)