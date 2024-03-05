with open('input.txt') as file:
    str = file.readline()
    list1 = str.split(' ')
    for str1 in list1:
        print(str1[::-1], end=" ")
file.close()