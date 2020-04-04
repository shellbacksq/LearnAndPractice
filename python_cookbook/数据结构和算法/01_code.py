"""
总结:
1. 用好列表推导式
2. 用好Python内置库 collections,itertools,operator
"""


# 序列赋值给多个变量
import heapq
a, b = (1, 2)

# 升级版，只想取开头或者结尾等特定位置的变量
first, *middle, last = (1, 2, 3, 4, 5, 6)

# 保留最后N个元素这里不是很清楚
# deque

# 查找最大或最小的N个元素
heapq.nlargest(3, [2, 3, 4, 1])
heapq.nsmallest(2, [3, 2, 4])

# 优先级队列(满足两个条件, 首先是队列，优先级相等时先进先出；然后，优先级高的先出)


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


a = [(-5, 1, Item('bar')), (-1, 0, Item('foo')), (-4, 2, Item('spam')), (-1, 3, Item('grok'))]
print(heapq.heappop(a))

q=PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q._queue)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# 元祖的元素可以比较
a=(1,0,Item('foo'))
b=(5,1,Item('bar'))
c=(1,1,Item('bar'))
print(a<b)
print(a<c)

# 字典中映射多个值
from collections import defaultdict
d=defaultdict(list)
d['a'].append(2)
print(d)

# 字典排序, 保持加入时候的顺序
from collections import OrderedDict

# 字典运算
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
price_sorted=sorted(zip(prices.values(),prices.keys()),reverse=True)
print(price_sorted)

# 字典的键或者值也支持集合操作

# 命名切片
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4]==items[a])

# 通过某个关键字排序一个字典列表
# itemgetter支持多个keys

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]

from operator import itemgetter

rows_by_fname=sorted(rows,key=itemgetter('fname'))
rows_by_uid=sorted(rows,key=itemgetter('uid'))

print(rows_by_fname,'\n',rows_by_uid)

#排序不支持原生比较的对象,attrgetter() 函数通常会运行的快点

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))

from operator import attrgetter
users=[User(3), User(23), User(99)]
sorted(users, key=attrgetter('user_id'))


# 通过某个字段将记录分组
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))
for date,items in groupby(rows,key=itemgetter('date')):
    print('date')
    for i in items:
        print(' ',i)


# 过滤序列元素

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([n for n in mylist if n > 0])

print((n for n in mylist if n > 0)) #生成式省内存,用filter也是生成式


