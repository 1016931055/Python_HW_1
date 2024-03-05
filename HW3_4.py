list1 = []
list2 = []
with open('input.txt') as file:
    wf = open('output.txt', 'w')
    num = file.readline()
    for i in range(int(num)):
        list1.append(file.readline().replace('\n',''))
    for i in range(int(num)):
        list2.append(file.readline().replace('\n',''))
    for x , y in zip(list1,list2):
        print(x,y, sep = '\t',file = wf)
file.close()
wf.close()