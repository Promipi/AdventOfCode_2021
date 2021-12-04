file_input = open("input_day_1.txt","r")
numbers = list(map(lambda x: int(x),file_input.readlines()))
count = 0
for index in range(1,len(numbers)):
    if(numbers[index] > numbers[index-1]):
        count +=1
print(count)