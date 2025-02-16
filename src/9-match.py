# 模式匹配
score = 'B'
if score >= 60:
    print('及格')
elif score >= 80:
    print('良好')
elif score >= 90:
    print('优秀')
else:
    print('不及格')

# match 模式匹配
match score:
    case 60:
        print('及格')
    case 80:
        print('良好')
    case 90:
        print('优秀')
    case _: # _表示匹配到其他任何情况
        print('不及格')