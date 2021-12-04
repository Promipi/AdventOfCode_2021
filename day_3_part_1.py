def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n

file_input = open("input_day_3.txt","r")
bins = []
for line in file_input.readlines():
    result = list(line.replace("\n",""))
    bins.append(result)

gamma = ""
elipson = ""

for column in range(0,len(bins[0])):
    total_column = []
    for row in range(0,len(bins)):
        total_column.append(bins[row][column])
    count_1 = total_column.count('1')
    count_0 = total_column.count('0')
    if(count_1 > count_0):
        gamma += "1"
    else:
        gamma += "0"

gamma_result = binaryToDecimal(int(gamma))
for c in gamma:
    if(c=='1'):
        elipson += "0"
    else:
        elipson += "1"

elipson_result = binaryToDecimal(int(elipson))
print(gamma_result*elipson_result)
