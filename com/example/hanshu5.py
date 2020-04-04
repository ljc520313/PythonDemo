
str="123456789"
# print(str[-1:-4:-1])
# print(str[-1:-4:-1])
# print(str[0:3:1])
# print(len(str))
# print(str[8:5:-1])
# for i in range(len(str)):
#     left = str[i-1:i-4:-1]
#     mid = str[i]
#     right = str[i+1:i+4:1]
#     print(left)
#     print(mid)
#     print(right)


# str1 = """
# sdsAAAkBBBhfsdshisCCCdFFFohudhudihAAsBBBcscdskjc
# scgisuhcsyguseRRRRiSSSSieugdisisossdudSEYEIEySDCDI
# """
# for i in range(len(str1)):
#     left = str[i,i-3,1]
#     mid = str[i]
#     right = str[i,i+3,1]

s = int(input('输入n'))
def jiec(s):

        for i in range(1,s):
            s = i*s
        return s

print(jiec(s))

递归
# def jie(n):
#     if n == 1:
#         return 1
#     else:
#         temp = n * jie(n - 1)
#         print(temp)
#         return temp

# n = int(input('输入n'))
# print(jie(n))
