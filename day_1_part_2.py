file_input = open("input_day_1.txt","r")
numbers = list(map(lambda x: int(x),file_input.readlines()))
sums = []
since = 0
until = 3
while(until <= len(numbers)):
    sums.append( sum(numbers[since:until]) )
    since+=1
    until+=1

count = 0
for index in range(1,len(sums)):
    if(sums[index] > sums[index-1]):
        count +=1
print(count)



