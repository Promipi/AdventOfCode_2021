input_file = open("input_day_6.txt","r")
fishes = {}
fishes_list = list(map(lambda x: int(x),input_file.readlines()[0].split(",")))
fishes_list.sort()
for n in range(-1,9):
    fishes[n] = 0

for fish in fishes_list:
    fishes[fish] = fishes_list.count(fish)


days = 256 
flag = False
for day in range(days):
    fishes[-1] = fishes[0]
    fishes[0] = fishes[1]
    fishes[1] = fishes[2]
    fishes[2] = fishes[3]
    fishes[3] = fishes[4]
    fishes[4] = fishes[5]
    fishes[5] = fishes[6]
    fishes[6] = fishes[7]
    fishes[7] = fishes[8]
    fishes[8] = fishes[-1]
    fishes[6] += fishes[-1]

total = sum(list(fishes.values()))
print(total-fishes[-1])