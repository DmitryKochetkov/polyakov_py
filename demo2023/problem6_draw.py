from turtle import *
left(90)

one = 30

for i in range(7):
    forward(10 * one)
    right(120)

pu()
for x in range(15):
    for y in range(15):
        goto(x * one, y * one)
        dot(5)
done()
