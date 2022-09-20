# filter()函数用于过滤序列，过滤掉不符合要求的元素，将满足要求的元素组织成新的列表返回
# filter(function, iterable)
# function - 判断函数
# iterable - 迭代对象

# 筛选出序列中为奇数的元素
def is_odd(n):
    return n % 2 == 1
result = filter(is_odd,range(10))
print(list(result))
print(list(result)) # 惰性计算：filter生成的迭代器仅可以使用一次

# 将filter和lambda结合，删除列表中的0
list_num = [1, 2, 3, 0, 8, 0, 3]
print(list(filter(lambda x: x, list_num)))  # 这里为什么会过滤掉0？因为filter会将iterable中的每个元素传递给function进行判断，判断结果为TRUE或FALSE，最终将TRUE的结果组成列表返回

def get_num(x):
    return x
print(list(filter(get_num, list_num)))

# 过滤列表元素中的大小写
list_word = ['A', 'e', 'I', 'o', 'U']
print(list(filter(lambda x: x.isupper(), list_word)))
print(list(filter(lambda x: x.islower(), list_word)))

import os
print(os.path.join(os.path.dirname(__file__),))

# 参考链接：
# 1.python 中的 filter() 函数——用于过滤序列，过滤掉不符合条件的元素，返回符合条件的元素组成新列表
# https://blog.csdn.net/weixin_44081384/article/details/122477513
# 2.python中的filter()函数
# https://blog.csdn.net/quanlingtu1272/article/details/95463171