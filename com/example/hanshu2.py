# for each in range(100,1000):
#     temp = each
#     sum = 0
#     while temp:
#         sum = sum + (temp%10)**3
#         temp = temp//10
#     print(sum)

def maxgy(x,y):
    if y > x:
        temp = x
        x = y
        y = temp

    while x%y != 0:
        z = x%y
        x = y
        y = z

    return y

x1 = int(input('输入第一个数'))
y1 = int(input('输入第二个数'))

print(maxgy(x1,y1))
