


if __name__ == '__main__':
    print("Hello World")

# 多行语句
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(total) # 输出为 6

# 字符串
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

str = '123456789'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

print(r'\n')      # 输出 \n

# 等待用户输入
input("\n\n按下 enter 键后退出。")

# 同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# 多个语句构成代码组
'''
    if expression : 
       suite
    elif expression : 
       suite 
    else : 
       suite
'''

# print 输出
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")   # a b
print()

# import 与 from...import
'''
    在 python 用 import 或者 from...import 来导入相应的模块。
    将整个模块(somemodule)导入，格式为： import somemodule
    从某个模块中导入某个函数,格式为： from somemodule import somefunction
    从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
    将某个模块中的全部函数导入，格式为： from somemodule import *
'''
# 导入 sys 模块
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

# 导入 sys 模块的 argv,path 成员
from sys import argv, path  # 导入特定的成员
print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path



# 命令行参数
# 很多程序可以执行一些操作来查看一些基本信息，Python可以使用-h参数查看各参数帮助信息：




# -----------------------------------------------------

# 多个变量赋值
# 变量定义
x = 10          # 整数
y = 3.14         # 浮点数
name = "Alice"   # 字符串
is_active = True # 布尔值

# 多变量赋值
a, b, c = 1, 2, "three"

# 查看数据类型
print(type(x))        # <class 'int'>
print(type(y))        # <class 'float'>
print(type(name))     # <class 'str'>
print(type(is_active)) # <class 'bool'>

# 标准数据类型
# Python3 的六个标准数据类型中：
    # 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
    # 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）

# 变量赋值
a, b, c = 1, 2, "runoob"

# 变量定义
x = 10          # 整数
y = 3.14         # 浮点数
name = "Alice"   # 字符串
is_active = True # 布尔值

# 查看数据类型
print(type(x))        # <class 'int'>
print(type(y))        # <class 'float'>
print(type(name))     # <class 'str'>
print(type(is_active)) # <class 'bool'>


a = 111
isinstance(a, int)
# isinstance 和 type 的区别在于：
#   type()不会认为子类是一种父类类型
#   isinstance()会认为子类是一种父类类型

# Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型
# Python 检测到你在用 is 比较一个字面量整数（如 1）和 True，这通常是代码错误（因为 is 比较的是身份，而不是值）
# Python 建议你使用 == 来比较值是否相等，除非你确实想检查是否是同一个对象

# 您也可以使用del语句删除一些对象引用 您可以通过使用 del 语句删除单个或多个对象
del a

# Python可以同时为多个变量赋值，如a, b = 1, 2
# 一个变量可以通过赋值指向不同类型的对象
# 数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数
# 在混合计算时，Python会把整型转换成为浮点数

# 字符串
# Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符
# 索引值以 0 为开始值，-1 为从末尾的开始位置
# 加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数
# Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
# 反斜杠(\)可以作为续行符，表示下一行是上一行的延续
# Python 字符串不能被改变。向一个索引位置赋值，比如 word[0] = 'm' 会导致错误










# Python解释器 解释你输入的Python代码
# 算数运算符
#   a**b 为10的21次方
#   // 取整除 - 往小的方向取整数

# 赋值运算符
#   := 海象运算符，这个运算符的主要目的是在表达式中同时进行赋值和返回赋值的值。Python3.8 版本新增运算符

# 位运算符
#   ~ 按位取反运算符

# 逻辑运算符
#   x and y 布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值
#   x or y  布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值
#   not x   布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True

# 成员运算符
#   in 如果在指定的序列中找到值返回 True，否则返回 False
#   not in 如果在指定的序列中没有找到值返回 True，否则返回 False

# 身份运算符
#   is 是判断两个标识符是不是引用自一个对象
#   is not 是判断两个标识符是不是引用自不同对象
#   id() 函数用于获取对象内存地址
#   is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等

# Python 数字运算
#   在交互模式中，最后被输出的表达式结果被赋值给变量

# 可以使用[]来截取字符串
var1 = 'Hello World!'
var2 = "Runoob"
print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

# 字符串格式化输出
# f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法
# >>> name = 'Runoob'
# >>> f'Hello {name}'  # 替换变量
# 'Hello Runoob'
# >>> f'{1+2}'         # 使用表达式
# '3'
#
# >>> w = {'name': 'Runoob', 'url': 'www.runoob.com'}
# >>> f'{w["name"]}: {w["url"]}'
# 'Runoob: www.runoob.com'

name = 'Runoob'
'Hello %s' % name

name = 'Runoob'
f'Hello {name}'  # 替换变量
f'{1+2}'         # 使用表达式
w = {'name': 'Runoob', 'url': 'www.runoob.com'}
f'{w["name"]}: {w["url"]}'

# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

# 列表
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[0] )
print( list[1] )
print( list[2] )
print( list[-1] )
print( list[-2] )
print( list[-3] )

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4])

list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]

# 读取第二位
print ("list[1]: ", list[1])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print ("list[1:-2]: ", list[1:-2])


list = ['Google', 'Runoob', 1997, 2000]
print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])
list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)


list = ['Google', 'Runoob', 1997, 2000]
print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)

# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表


# 列表比较
# 导入 operator 模块
import operator
a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))

# 元祖
# Python 的元组与列表类似，不同之处在于元组的元素不能修改
# 元组使用小括号 ( )，列表使用方括号 [ ]
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可

tup1 = () # 创建空元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 删除元祖
tup = ('Google', 'Runoob', 1997, 2000)
print(tup)
del tup
print("删除后的元组 tup : ")
# 所谓元组的不可变指的是元组所指向的内存中的内容不可变

# Python3 字典
#   键必须是唯一的，但值则不必
#   值可以取任何数据类型，但键必须是不可变的，如字符串，数字

# 使用大括号 {} 来创建空字典
emptyDict = {}
# 打印字典
print(emptyDict)
# 查看字典的数量
print("Length:", len(emptyDict))
# 查看类型
print(type(emptyDict))

# 使用内建函数 dict() 创建字典
emptyDict = dict()
# 打印字典
print(emptyDict)
# 查看字典的数量
print("Length:", len(emptyDict))
# 查看类型
print(type(emptyDict))

# 访问字典里的值
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])

# 修改字典
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
tinydict['Age'] = 8  # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息
print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

# 删除字典元素
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del tinydict['Name']  # 删除键 'Name'
tinydict.clear()  # 清空字典
del tinydict  # 删除字典
print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

# 字典键的特性
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行
# 两个重要的点需要记住：
#   不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
#   键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行


# Python3 集合
#   集合（set）是一个无序的不重复元素序列
#   集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作
#   可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合
#   创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
'orange' in basket
'crabgrass' in basket


# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
a
# {'a', 'r', 'b', 'c', 'd'}
a - b                              # 集合a中包含而集合b中不包含的元素
# {'r', 'd', 'b'}
a | b                              # 集合a或b中包含的所有元素
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # 集合a和b中都包含了的元素
# {'a', 'c'}
a ^ b                              # 不同时包含于a和b的元素
# {'r', 'd', 'b', 'm', 'z', 'l'}


# 类似列表推导式，同样集合支持集合推导式(Set comprehension):
a = {x for x in 'abracadabra' if x not in 'abc'}
a
# {'r', 'd'}

# 集合
set1 = {1, 2, 3, 4}            # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])      # 使用 set() 函数从列表创建集合
# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典

# 新增
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

thisset.update({1,3})
print(thisset)

# 移除
thisset.remove("Taobao") # 不存在会发生错误
print(thisset)

thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)

# 随机删除一个元素
x = thisset.pop()
print(x)

# 计算集合元素个数
thisset = set(("Google", "Runoob", "Taobao"))
len(thisset)

# 清空集合
thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear()
print(thisset)

# 判断元素是否在集合中存在
thisset = set(("Google", "Runoob", "Taobao"))
"Runoob" in thisset

# 条件控制语句
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")

# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

# case _: 类似于 C 和 Java 中的 default:，当其他 case 都无法匹配时，匹配这条，保证永远会匹配成功
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

mystatus=400
print(http_error(400))

# 循环语句
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))

count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

# for 循环
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)

# 也可用于打印字符串中的每个字符
word = 'runoob'
for letter in word:
    print(letter)

# 整数范围值可以配合 range() 函数使用
#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)

for x in range(6):
  # 循环主体
  print(x)
else:
  # 循环结束后执行的代码
  print("Finally finished!")

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# 也可以使 range() 以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')
for i in range(0, 10, 3) :
    print(i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

# break语句的使用
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')

for letter in 'Runoob':  # 第一个实例
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('当前变量值 :', var)
print("Good bye!")

# Python pass是空语句，是为了保持程序结构的完整性
# pass 不做任何事情，一般用做占位语句

# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

# Python 推导式
# 列表推导式
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names)

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 字典推导式
listdemo = ['Google','Runoob', 'Taobao']
newdict = {key:len(key) for key in listdemo}
newdict
# {'Google': 6, 'Runoob': 6, 'Taobao': 6}

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典
dic = {x: x**2 for x in (2, 4, 6)}
dic
# {2: 4, 4: 16, 6: 36}

# 集合推导式
setnew = {i**2 for i in (1,2,3)}
setnew
# {1, 4, 9}

a = {x for x in 'abracadabra' if x not in 'abc'}
a
# {'d', 'r'}

# 元组推导式（生成器表达式）
a = (x for x in range(1,10))
tuple(a)       # 使用 tuple() 函数，可以直接将生成器对象转换成元组
# (1, 2, 3, 4, 5, 6, 7, 8, 9)

# 代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退
# 迭代器有两个基本的方法：iter() 和 next()
# 字符串，列表或元组对象都可用于创建迭代器
list=[1,2,3,4]
it = iter(list)
print (next(it))

for x in it:
    print (x, end=" ")

while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()

# Python3 迭代器与生成器
# 迭代器有两个基本的方法：iter() 和 next()
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
# _iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成
# __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象
# 如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


##### 生成器
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）
# yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果
# 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
# 当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回
# 每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果
# 调用一个生成器函数，返回的是一个迭代器对象

# yield 的使用案例如下
import sys
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

# with 关键字为我们提供了一种优雅的方式来处理文件操作、数据库连接等需要明确释放资源的场景
# with 语句的优势
#   自动资源释放：确保资源在使用后被正确关闭
#   代码简洁：减少样板代码
#   异常安全：即使在代码块中发生异常，资源也会被正确释放
#   可读性强：明确标识资源的作用域
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# 文件已自动关闭

# with 语句的工作原理
# with 语句背后是 Python 的上下文管理协议，该协议要求对象实现两个方法：
#   __enter__()：进入上下文时调用，返回值赋给 as 后的变量
#   __exit__()：退出上下文时调用，处理清理工作
#       __exit__() 方法接收三个参数：
#           exc_type：异常类型
#           exc_val：异常值
#           exc_tb：异常追踪信息
#       如果 __exit__() 返回 True，则表示异常已被处理，不会继续传播；返回 False 或 None，异常会继续向外传播

# 文件操作
# 同时打开多个文件
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content.upper())

# 数据库连接
import sqlite3
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()

# 线程锁
import threading
lock = threading.Lock()
with lock:
    # 临界区代码
    print("这段代码是线程安全的")

# 临时修改系统状态
import decimal
with decimal.localcontext() as ctx:
    ctx.prec = 42  # 临时设置高精度
    # 执行高精度计算
# 精度恢复原设置

# 创建自定义的上下文管理器
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"耗时: {self.end - self.start:.2f}秒")
        return False

# 使用示例
with Timer() as t:
    # 执行一些耗时操作
    sum(range(1000000))

# Python 的 contextlib 模块提供了更简单的方式来创建上下文管理器
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

# 使用示例 传统资源管理的问题
with tag("h1"):
    print("这是一个标题")

# 优势
#   自动资源释放：确保资源在使用后被正确关闭
#   代码简洁：减少样板代码
#   异常安全：即使在代码块中发生异常，资源也会被正确释放
#   可读性强：明确标识资源的作用域

# with 语句背后是 Python 的上下文管理协议，该协议要求对象实现两个方法：
#   __enter__()：进入上下文时调用，返回值赋给 as 后的变量
#   __exit__()：退出上下文时调用，处理清理工作 __exit__() 方法接收三个参数：
#       exc_type：异常类型
#       exc_val：异常值
#       exc_tb：异常追踪信息
#   如果 __exit__() 返回 True，则表示异常已被处理，不会继续传播；返回 False 或 None，异常会继续向外传播

# 文件操作
# 同时打开多个文件
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content.upper())

# 数据库连接
import sqlite3
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
# 连接自动关闭

# 线程锁
import threading
lock = threading.Lock()
with lock:
    # 临界区代码
    print("这段代码是线程安全的")

# 临时修改系统状态
import decimal
with decimal.localcontext() as ctx:
    ctx.prec = 42  # 临时设置高精度
    # 执行高精度计算
# 精度恢复原设置

# 创建自定义的上下文管理器
#   我们可以通过实现 __enter__ 和 __exit__ 方法创建自定义的上下文管理器：
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"耗时: {self.end - self.start:.2f}秒")
        return False

# 使用示例
with Timer() as t:
    # 执行一些耗时操作
    sum(range(1000000))

# Python 的 contextlib 模块提供了更简单的方式来创建上下文管理器：
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")  # __enter__()
    yield   # 执行代码逻辑
    print(f"</{name}>") # __exit__()

# 使用示例
with tag("h1"):
    print("这是一个标题")

# 最佳实践
#   优先使用 with 管理资源：对于文件、网络连接、锁等资源，总是优先考虑使用 with 语句
#   保持上下文简洁：with 块中的代码应该只包含与资源相关的操作
#   合理处理异常：在自定义上下文管理器中，根据需求决定是否抑制异常
#   利用多个上下文：Python 允许在单个 with 语句中管理多个资源

# 函数 可更改(mutable)与不可更改(immutable)对象
#   不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象
#   可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)

# 函数中传递参数
#   必需参数 # printme()
#   关键字参数 # printme( str = "菜鸟教程")
#   默认参数 # def printinfo( name, age = 35 ):
#   不定长参数 # def printinfo( arg1, *vartuple ): *vartuple 可以接收多个参数
#       加了两个星号 ** 的参数会以字典的形式导入
# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)

# 调用 printinfo 函数
printinfo(1, a=2, b=3)


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total
# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)

# 强制位置参数

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]


from functools import reduce
numbers = [1, 2, 3, 4, 5]
# 使用 reduce() 和 lambda 函数计算乘积
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 输出：120

# Python 装饰允许在不修改原有函数代码的基础上，动态地增加或修改函数的功能
#   装饰器本质上是一个接收函数作为输入并返回一个新的包装过后的函数的对象
# 装饰器的应用场景：
#   日志记录: 装饰器可用于记录函数的调用信息、参数和返回值
#   性能分析: 可以使用装饰器来测量函数的执行时间
#   权限控制: 装饰器可用于限制对某些函数的访问权限
#   缓存: 装饰器可用于实现函数结果的缓存，以提高性能
# 伪代码如下:
# def decorator_function(original_function):
#     def wrapper(*args, **kwargs):
#         # 这里是在调用原始函数前添加的新功能
#         before_call_code()
#         result = original_function(*args, **kwargs)
#         # 这里是在调用原始函数后添加的新功能
#         after_call_code()
#         return result
#     return wrapper
# # 使用装饰器
# @decorator_function
# def target_function(arg1, arg2):
#     pass  # 原始函数的实现
def my_decorator(func):
    def wrapper():
        print("在原函数之前执行")
        func()
        print("在原函数之后执行")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 带参数的装饰器
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("在原函数之前执行")
        func(*args, **kwargs)
        print("在原函数之后执行")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 装饰器本身也可以接受参数，此时需要额外定义一个外层函数
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()

# 类装饰器（Class Decorator）是一种用于动态修改类行为的装饰器，它接收一个类作为参数，并返回一个新的类或修改后的类
# 类装饰器可以用于：
#   添加/修改类的方法或属性
#   拦截实例化过程
#   实现单例模式、日志记录、权限检查等功能
# 类装饰器有两种常见形式：
#   函数形式的类装饰器（接收类作为参数，返回新类）
#   类形式的类装饰器（实现 __call__ 方法，使其可调用）

# 类装饰器
def log_class(cls):
    """类装饰器，在调用方法前后打印日志"""
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)  # 实例化原始类
        def __getattr__(self, name):
            """拦截未定义的属性访问，转发给原始类"""
            return getattr(self.wrapped, name)
        def display(self):
            print(f"调用 {cls.__name__}.display() 前")
            self.wrapped.display()
            print(f"调用 {cls.__name__}.display() 后")
    return Wrapper  # 返回包装后的类

@log_class
class MyClass:
    def display(self):
        print("这是 MyClass 的 display 方法")

obj = MyClass()
obj.display()

# 类形式的类装饰器（实现 __call__ 方法） 单例模式
class SingletonDecorator:
    """类装饰器，使目标类变成单例模式"""
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
    def __call__(self, *args, **kwargs):
        """拦截实例化过程，确保只创建一个实例"""
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

@SingletonDecorator
class Database:
    def __init__(self):
        print("Database 初始化")

db1 = Database()
db2 = Database()
print(db1 is db2)  # True，说明是同一个实例

# 内置装饰器
#   @staticmethod: 将方法定义为静态方法，不需要实例化类即可调用
#   @classmethod: 将方法定义为类方法，第一个参数是类本身（通常命名为 cls）
#   @property: 将方法转换为属性，使其可以像属性一样访问
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")
    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}.")
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
# 使用
MyClass.static_method()
MyClass.class_method()
obj = MyClass()
obj.name = "Alice"
print(obj.name)

# 多个装饰器的堆叠
#   你可以将多个装饰器堆叠在一起，它们会按照从下到上的顺序依次应用
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper
def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper
@decorator1
@decorator2
def say_hello():
    print("Hello!")
say_hello()


# 数据结构实现栈 栈的数据结构 使用列表实现栈
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

# 使用示例
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("栈顶元素:", stack.peek())  # 输出: 栈顶元素: 3
print("栈大小:", stack.size())    # 输出: 栈大小: 3
print("弹出元素:", stack.pop())  # 输出: 弹出元素: 3
print("栈是否为空:", stack.is_empty())  # 输出: 栈是否为空: False
print("栈大小:", stack.size())    # 输出: 栈大小: 2


# 使用列表实现队列
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from empty queue")
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)

# 使用示例
queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print("队首元素:", queue.peek())    # 输出: 队首元素: a
print("队列大小:", queue.size())    # 输出: 队列大小: 3
print("移除的元素:", queue.dequeue())  # 输出: 移除的元素: a
print("队列是否为空:", queue.is_empty())  # 输出: 队列是否为空: False
print("队列大小:", queue.size())    # 输出: 队列大小: 2

# 模块 模块的作用
#   代码复用：将常用的功能封装到模块中，可以在多个程序中重复使用
#   命名空间管理：模块可以避免命名冲突，不同模块中的同名函数或变量不会互相干扰
#   代码组织：将代码按功能划分到不同的模块中，使程序结构更清晰
import sys
print('命令行参数如下:')
for i in sys.argv:
    print(i)
print('\n\nPython 路径为：', sys.path, '\n')

# import 语句
# 导入模块
# import support

# 给模块起别名
import numpy as np  # 将 numpy 模块别名设置为 np
from math import sqrt as square_root  # 将 sqrt 函数别名设置为 square_root

# 模块名称
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
# 说明：每个模块都有一个 __name__ 属性
#   如果模块是被直接运行，__name__ 的值为 __main__
#   如果模块是被导入的，__name__ 的值为模块名
#   说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格





















