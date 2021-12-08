input_file = open("input_day_7.txt","r")
def fac_sum(n):
    return n+( n*(n-1) / 2)

crabs = list(map(lambda x:int(x),input_file.readlines()[0].split(",")))
min = 10**100000
for fuel in range(1,max(crabs)):
    total = 0
    for crab in crabs:
        total += fac_sum(abs(crab - fuel))
    if(total < min):
        min = total

print(int(min))