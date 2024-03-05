import itertools as it
with open('studygroup.txt') as file:
    list = file.readline().split(' ')
    for x,y,z in it.combinations(list,3):
        print('1:', x , '2:', y ,'3:' ,z ,sep=' ')
