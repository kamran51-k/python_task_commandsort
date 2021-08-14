def command_sort():
    a = input()
    a = a.split(' ')
    list1 = []
    for i in a:
        i = int(i)
        list1.append(i) 
        list1 = sorted(list1)
    print(list1)
command_sort()

    

    
    
