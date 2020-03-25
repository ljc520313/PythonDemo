
def findstr(x1,x2):
    i = 0
    k=x1.find(x2)
    while(k!=-1):
        i += 1
        k=x1.find(x2,k+1)
    return i

str1 = 'i want to improve python,improve python once time im'
str2 = 'im'

print(findstr(str1,str2))

