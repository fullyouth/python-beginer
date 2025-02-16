# list
# 1. 列表的创建
# 1.1 直接创建
a = [1, 2, 3, 4, 5]
print(a)
print(type(a))

# 1.2 利用list()函数
b = list(range(1, 10, 2))
print(b)
print(type(b))

# 2. 列表的访问
# 2.1 直接访问
print(a[0])
print(a[1])

# 3. 列表的操作
# 3.1 列表的拼接
c = a + b
print(c)

# 3.2 列表的复制
d = a * 3
print(d)

# 3.3 列表的切片
print(a[1:3])
print(a[1:])
print(a[:3])
print(a[::2])
print(a[::-1])

# 3.4 列表的排序
a.sort()
print(a)

# 3.5 列表的反转
a.reverse()
print(a)

# 3.6 列表的插入
a.insert(0, 0)
print(a)

# 3.7 列表的删除
a.remove(0)
print(a)

# 3.8 列表的清空
a.clear()
print(a)

# 3.9 列表的查找
print(a.index(1))

# 3.10 列表的统计
print(a.count(1))

# 3.11 列表的复制
e = a.copy()
print(e)

# append 追加元素到末尾
a.append(1)
print(a)
# pop 弹出末尾元素
a.pop()
print(a)

# pop 弹出指定位置元素
a.pop(0)
print(a)

# remove 移除指定元素
a.remove(1)
print(a)

# insert 插入指定位置元素
a.insert(0, 1)
print(a)
