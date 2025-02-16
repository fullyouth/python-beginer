# dict 字典
# 字典 dict 全称 dictionary，在其他语言中也称为 map，使用键-值（key-value）存储，具有极快的查找速度
# 定义一个字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 把数据放入 dict 的方法，除了初始化时指定外，还可以通过 key 放入
d['Adam'] = 67
print(d['Adam'])

# 增删改查
# 由于一个 key 只能对应一个 value，所以，多次对一个 key 放入 value，后面的值会把前面的值冲掉
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88

# 删除一个 key，用 pop(key) 方法，对应的 value 也会从 dict 中删除
d.pop('Bob')
print(d)

# 遍历
# 遍历 dict 时，使用 for...in 循环，由于 dict 的存储不是按照 list 的方式顺序排列，所以，迭代出的结果顺序很可能不一样
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# 遍历 value
for value in d.values():
    print(value)

# 遍历 key 和 value
for k, v in d.items():
    print(k, v)

#Set 集合
#set 和 dict 类似，也是一组 key 的集合，但不存储 value。由于 key 不能重复，所以，在 set 中，没有重复的 key
s = set([1, 2, 3])
print(s)

# 通过 add(key) 方法可以添加元素到 set 中，可以重复添加，但不会有效果
s.add(4)
print(s)
# 通过 remove(key) 方法可以删除元素
s.remove(4)
print(s)
# set 可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

