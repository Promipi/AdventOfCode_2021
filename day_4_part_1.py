file_input = open("input_day_4.txt","r")
def is_table_completed(table):
    for row in range(0,len(table[0])):
        if(list(table[row].values()).count(True)==5):
            return (True,table[row])
    for column in range(0,len(table[0])):
        count = 0
        column_list = []
        for row in range(0,len(table[0])):
            value = table[row][list(table[row].keys())[column]]
            if(value==True):
                column_list.append(list(table[row].keys())[column])
                count += 1
        if(count==5):
            return (True,column_list)
        column_list.clear()
        count = 0
    return (False,[])

def split_line(line):
    result = []
    num = ""
    for index in range(0,len(line)-1):
        
        if( (line[index]==' ' or line[index]=='\n') and line[index+1]!=' ' and index!=0):
            result.append(num)
            num = ""
        else:
            num += line[index]
    result.append(num)
    return result

def marcar():
    for number in numbers:
        for table in range(0,lenght):
            for row in range(0,5):
                for num in tables[table][row]:
                    if(num == number):
                        tr[table][row][num] = True
        for index_table in range(0,len(tables)):
            (value,lista) = is_table_completed(tables[index_table])
            if(value == True):
                sum_win = sum(list(lista.keys()))
                total = 0
                for line in tables[index_table]:
                    for key in line:
                        if(line[key]==False):
                            total += key
                print(total*number)
                return True

tables = []
numbers = []
last_number_called = 0
sum_without_mark = 0

index = 0
table_aux = []
for line in file_input.readlines():
    if(index==0):
        numbers = list(map(lambda x: int(x),line.split(",")))
    else:
        if(line=="\n" and index!=1):
            tables.append(table_aux.copy())
            table_aux.clear()
        else:
            if(index!=1):
                line_splited = split_line(list(line))
                line_splited = map(lambda x: int(x),line_splited)
                line_dict = {}
                for num in line_splited:
                    line_dict[num] = False
                table_aux.append(line_dict)
    index += 1

tr = tables.copy()
lenght = len(tables)
marcar()


