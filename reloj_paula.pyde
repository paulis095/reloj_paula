m = 0
p = 0
s = 0
def setup ():
    size (200, 200)
def draw():
    background(0)
    global m
    global p
    global s
    square(10, m, 40)
    if m > height:
       m = 0
    else:
       m = map(second(), 0, 59, 0, height)
    square(80, p, 40)
    if p > height:
       p = 0
    else:
       p = map(minute(), 0, 59, 0, height)
    square(150, s, 40)
    if s > height:
       s = 0
    else:
       s = map(hour(), 0, 59, 0, height)
