file_input = open("input_day_2.txt","r")
#part1
x = 0; y = 0
for line in file_input.readlines():
    [instruction,value] = line.split(" ")
    if(instruction=="forward"):
        x += int(value)
    elif(instruction=="up"):
        y -= int(value)
    elif(instruction=="down"):
        y += int(value)
print(x*y)