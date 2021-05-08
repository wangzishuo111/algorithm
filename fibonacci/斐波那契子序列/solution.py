l1 = [1,2,3,4,5,6,7,8]
l1 = [1,3,7,11,12,14,18]

myset = set()
for i in l1:
    myset.add(i)

for i in range(len(l1)):
    for j in range(i+1, len(l1)):
        mylist = []
        first = l1[i]
        second = l1[j]
        while first + second in myset:
            if first not in mylist:
                mylist.append(first)
            if second not in mylist:
                mylist.append(second)
            a = second
            second = first + second
            if second not in mylist:
                mylist.append(second)
            first = a

        if mylist:
            print (mylist)
