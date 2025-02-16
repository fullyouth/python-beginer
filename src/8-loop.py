# 循环
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
