hobbies=""
for i in range (3):
    s=input ('请输入你的小爱好(最多三个，按q或者Q结束)：')
    if s.upper()=='q':
        break
    hobbies += s+ ''
print('你的小爱好是：',hobbies)
