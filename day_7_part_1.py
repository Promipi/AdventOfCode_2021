input_file = open("input_day_7.txt","r")
crabs = list(map(lambda x:int(x),input_file.readlines()[0].split(",")))
min = 10**10000
for fuel in range(1,max(crabs)):
    total = 0
    for crab in crabs:
        total += abs(crab - fuel)
    if(total < min):
        min = total
print(min)