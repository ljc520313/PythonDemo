member = ['甲','乙','丙','丁','伍']
list_num = [88,90,85,90,88]

for i in range(0,10):
    if i%2 == 0:
        member.insert(i+1,list_num[i//2])

print(member)

# i:     0  2  4  6  8
# index:
#li:
