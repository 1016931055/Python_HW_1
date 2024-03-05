with open('input.txt') as file:
    for line in file:
        list = line.split(' ')
        for str in list[::2]:
            print( str.replace('\n',''), end = ' ')
        print()



