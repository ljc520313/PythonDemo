

str1 = """#$%^&*()#$%&@##
)))}}""".replace("\n","")
list1 =[]
list2 =[]
for i in str1:
    if i in list1:
        list2[list1.index(i)] = list2[list1.index(i)] + 1
    else:
        list1.append(i)
        list2.append(1)

print(list1)
print(list2)
for i in list1:
    print('字符%s出现了%s次'%(i,str(list2[list1.index(i)])))


