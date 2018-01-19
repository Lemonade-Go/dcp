"""
solution to d14
author: david white
date: 01-18-2018

Monte Carlo: based off N number of random guesses, an approx. solution can be reached

Lessons Learned:
    - What monte carlo was
"""

#import python 3 division to allow float
from __future__ import division
import random


def monte_carlo():
    #Assume radius == 1
    x = random.random()
    y = random.random()
    #print(x ** 2 + y ** 2) ##DEBUG
    return x**2 + y**2 < 1

def estimate_pi(num_of_tries):
    percentage_in_circle = 0
    for _ in range(num_of_tries):
        if(monte_carlo()):
            percentage_in_circle += 1
    tmp = percentage_in_circle / num_of_tries
    
    #multiply by 4 to simulate full circle 
    #we only tested (x,y) of [(-x,y),(-x,-y),(x,-y),(x,y)]
    return tmp*4

if __name__ == "__main__":
    #increasing num_of_tries gets closer to real value
    num_of_tries = 1000000
    print("%.3f" % estimate_pi(num_of_tries))


