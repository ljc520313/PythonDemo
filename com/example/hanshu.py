def poo(x,y):
    zz=1
    k=1
    # while(k<=y):
    #     zz*=x
    #     k+=1
    for i in range(0,y):
        zz = zz*x
    return zz



x = int(input('请输入底数'))
y = int(input('请输入幂数'))
zz = poo(x,y)
print('结果为:'+ str(zz))