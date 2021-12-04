
def more(matrix,column):
    total_column = []
    for row in range(0,len(matrix)):
        total_column.append(matrix[row][column])

    (count_1,count_0) = (total_column.count('1'),total_column.count('0') )

    return (count_0,count_1)

def filter_bins(bit1,bit2,iterator):
    for column in range(0,len(bins[0])):
        (count_0,count_1) = more(iterator,column)
        if(count_0 > count_1):
            iterator = list(filter(lambda x: x[column] == str(bit1) ,iterator))
        else:
            iterator = list(filter(lambda x: x[column] == str(bit2),iterator))
        if(len(iterator)==1):
            return iterator


file_input = open("input_day_3.txt","r")
bins = []
for line in file_input.readlines():
    result = line.replace("\n","")
    bins.append(result)

oxigens = bins.copy()
depurators = bins.copy()

oxigens = filter_bins(0,1,oxigens)
result_oxigen = int( oxigens[0] , 2 )

depurators = filter_bins(1,0,depurators)
result_deputrator =int( depurators[0] , 2 )

print(result_deputrator*result_oxigen)
