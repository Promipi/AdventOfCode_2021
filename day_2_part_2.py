file_input = open("input_day_2.txt","r")
#part2
x = 0; y = 0
objective = 0
for line in file_input.readlines():
    [instruction,value] = line.split(" ")
    if(instruction=="forward"):
        x += int(value)
        y += (objective * int(value))
    elif(instruction=="up"):
        objective -= int(value)
    elif(instruction=="down"):
        objective += int(value)
print(x*y)