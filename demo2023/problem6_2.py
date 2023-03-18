from turtle import *
color('black', 'red')
speed(10000)

one = 10

begin_fill()
left(90)
for i in range(2):
    forward(10 * one)
    right(90)
    forward(20 * one)
    right(90)
end_fill()

forward(3 * one)
right(90)
forward(5 * one)
left(90)

begin_fill()
for i in range(2):
    forward(70 * one)
    right(90)
    forward(80 * one)
    right(90)
end_fill()

canvas = getcanvas()
c = 0

for x in range(100):
    for y in range(100):
        # goto(x * one, y * one)
        # dot(5)

        x_fixed = x * one
        y_fixed = y * one

        point = canvas.find_overlapping(x_fixed, y_fixed, x_fixed, y_fixed)
        if len(point) == 1 and point[0] == 5:
            c += 1

print(c)
done()
exit()