
tr = input('猜猜我是谁？')
guess = int(tr)
x = 1

while  guess != 8 and  x < 3:

        if guess > 8 :
            print('大了')
        else:
            print('小了')

        tr = input('再猜猜？')
        guess = int(tr)
        x = x + 1

if  guess == 8:
    print('对了')
else:
    print('三次机会都错')



