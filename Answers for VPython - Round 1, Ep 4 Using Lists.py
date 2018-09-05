from vpython import *

my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(5)
my_list.append("Hello")
my_list.append(box())
my_list.append(my_list[4].pos)

print(my_list)

my_list[4].color = color.red

list_of_boxes = []

x = 0
while x < 20:
    list_of_boxes.append(box(pos=vector(x,0,0), color = color.red))
    x = x + 2
list_of_boxes[3].color = color.blue
list_of_boxes[3].pos.z = -1

two_dimen_list = []

two_dimen_list.append([0,1,5])
two_dimen_list.append([3,1,4])
two_dimen_list.append([3,7,9])
print(two_dimen_list[2][1])