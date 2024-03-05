with open('input.txt') as file:
    for line in file:
        if('ё' in line):
            print(line, end='')
file.close()