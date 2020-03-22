

password = input('请输入密码：')
list1 = ['&','*','#','~']

strqd=""

for i in password:
    if i.isdigit():
        strqd+='1'
    elif i.isalpha():
        strqd+='2'
    elif i in list1:
        strqd+='3'

if len(password)>=16 and password[0].isalpha() and '1' in strqd and '2' in strqd and '3' in strqd:
    print("密码安全级别为高")
elif len(password)>=8 and ('1' in strqd and '2' in strqd or '3' in strqd and '1' in strqd or '2'  in  strqd and '2' in strqd):
    print("密码安全级别为中")
elif len(password)<=8 and ('1' in strqd or '2' in strqd):
    print('密码安全级别为低')













#
# if size==len(password):
#     print("密码安全级别为高")

# if len(password) >= 16 and password.isalnum():
#     print('密码安全级别为低')
# elif len(password)<=8 and (password.isalpha() and password.isdigit() or password.isalpha() and password.isdigit() or password.isalpha() and password.isdigit() ):
#     print('密码安全级别为中')
# elif password.isalpha() and i in list1:

# £    if 数值 and 字符 or 数值 and 特殊字母 or 字母 and 特殊字符
#       password.isalpha() //仅由字母构成
#       password.isdigit() //仅由数字构成
#       list1 = ['&','*','#','~']
