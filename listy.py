numbers = [3, 6, 4, 7, 6, 2]

numbers.append(9)
numbers.remove(6)
numbers.insert(0, 0)
numbers.sort()
print(numbers)

def list():
    my_list = []
    for i in range(3):
        my_list.append(int(input("prvek seznamu")))
    new_list = my_list.copy()
    new_list.sort()
    return my_list == new_list

#print(list())
list=[1, 2, 3, 4]
#print(list[2:3])

vnoreny_seznam = []
for i in range(10):
    seznam = []
    for j in range(10):
        seznam.append(i + j)
    vnoreny_seznam.append(seznam)
print(vnoreny_seznam)

def column_sums(table):
    final_list = []
    for i in range(3):
        list = []
        for j in range(3):
            list.append(table[0][j] + table[1][j] + table[2][j])
        final_list.append(list)
    return final_list
print(column_sums([[5, 3, 8], [5, 10, 1], [3, 8, 12]]))