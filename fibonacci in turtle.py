from turtle import *
from math import *
from itertools import cycle

colors = ["black","red", "orange", "yellow", "green", "blue"]

def fibonacci(n):
  if n <= 0:
    return [0]
  s = [0, 1]
  while len(s) <= n:
    next_value = s[len(s) - 1] + s[len(s) - 2]
    s.append(next_value)
  return s

x=list(fibonacci(8))
print(x) 
colors = cycle(colors)

for i in x:
    for j in range(i):
        circle(100)
        left(3)
    color(next(colors))     
    left(20)
exitonclick()