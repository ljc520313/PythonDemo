# str1 = '上海自来水来自海上'
# str1 = '如来佛祖'
str1 = input('输入一个句子判断是否是回文：')
str_list = list(str1)
str_list1 = str_list
# str_list1 = list(str1)
str_list.reverse()
# reverse()只作用于列表不作用于字符串
print(str_list)
print(str_list1)

if str_list1 == str_list:
    print('字符串%s是回文联'%str1)
else:
    print('字符串%s不是回文联'%str1)



# 方法2
# k=0
# for i in range(0,len(str)//2):
#     if str[i] == str[len(str)-1-i]:
#         k+=1
#
# if(len(str)//2==k):
#     print(k)


