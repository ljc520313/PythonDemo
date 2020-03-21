name = input('输入待查名字：')
score = [['小明',60],['小红',90],['小兰',100]]
for each in score:
    if name in each[0]:
        print(name +"的得分为"+ str(each[1]))
        break

if name not in each[0]:
    print('名字不存在')


#
# if name not in [s[0] for s in score]:
#     print('名字不存在')

