input_file = open("input_day_6.txt","r")
fishes = list(map(lambda x: int(x),input_file.readlines()[0].split(",")))
print(fishes)
num_days = 80
for day in range(0,num_days):
    fishes = list(map(lambda f: f-1,fishes))
    for index in range(0,len(fishes)):
        if(fishes[index]==-1):
            fishes[index] = 6
            fishes.append(8)
print(len(fishes))