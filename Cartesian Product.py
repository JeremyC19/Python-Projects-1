list1 = [10, 20]
list2 = [1, 2, 3, 4]

i = 0
j = 0

list3 = ['(' + str(i) + ', ' + str(j) + ')' for i in list1 for j in list2]

print(list3)
