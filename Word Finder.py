lst = [5, 2, 'T', 8, 4, 125, 23, 'h', 6, 0, 'e', 543, 5, 's', 2, 4, 'e', 4, 6, 'c', 'r', 5, 67, 2, 'e', 't', 9, 'c', 2, 7, 'o', 4, 2, 'd', 'e', 3]
ind = 0
permanent_arr = []  # creates an array to store verified string characters
temporary_arr = []  # creates an array to temporarily store string characters until other types of characters are found
while ind < len(lst):  # ensures that the index will go to the full length of the list
    cur_element = lst[ind]  # sets cur_element equal to the 'ind' element of the list
    if (isinstance(cur_element, str) == True):  # checks to see if the current element of the list is a string
        temporary_arr.append(cur_element)  # appends the current value in the list to temporary_arr
    else:
        if len(temporary_arr) != 0:  # checks to see if the length of one_d_arr is not equal to zero
            permanent_arr.append(temporary_arr)  # if so, temporary_arr gets appended to permanent_arr
        temporary_arr = []  # resets the values of temporary_arr to allow new values in the list to be appended
    ind = ind + 1

print(permanent_arr)
