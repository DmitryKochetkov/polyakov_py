from turtle import *
color('black', 'red')
speed(10000)

one = 30

begin_fill()
left(90)
for i in range(3):
    forward(10 * one)
    right(120)
end_fill()

canvas = getcanvas()
c = 0

for x in range(-15, 15):
    for y in range(-15, 15):
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