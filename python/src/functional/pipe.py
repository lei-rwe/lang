# pipeline 管道借鉴于Unix Shell的管道操作——把若干个命令串起来，
# 前面命令的输出成为后面命令的输入，如此完成一个流式计算。
# （注：管道绝对是一个伟大的发明，他的设哲学就是KISS – 让每个功能
# 就做一件事，并把这件事做到极致，软件或程序的拼装会变得更为简单和直观。
# 这个设计理念影响非常深远，包括今天的Web Service，云计算，
# 以及大数据的流式计算等等）

# 比如，我们如下的shell命令：
# ps auwwx | awk '{print $2}' | sort -n | xargs echo

#如果我们抽象成函数式的语言，就像下面这样：
# xargs(  echo, sort(n, awk('print $2', ps(auwwx)))  )

# 也可以类似下面这个样子：
# pids = for_each(result, [ps_auwwx, awk_p2, sort_n, xargs_echo])

# 我们先来看一个如下的程序，这个程序的process()有三个步骤：
#        1）找出偶数。
#        2）乘以3
#        3）转成字符串返回

def process(num):
    # filter out non-evens
    if num % 2 != 0:
        return
    num = num * 3
    num = 'The Number: %s' % num
    return num

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    print(process(num))

# 我们来看看函数式的pipeline（第一种方式）应该怎么写
def even_filter(nums):
    for num in nums:
        if num % 2 == 0:
            yield num
def multiply_by_three(nums):
    for num in nums:
        yield num * 3
def convert_to_string(nums):
    for num in nums:
        yield 'The Number: %s' % num

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipeline = convert_to_string(multiply_by_three(even_filter(nums)))
for num in pipeline:
    print(num)


# 根据前面的原则——“使用Map & Reduce，不要使用循环”
def even_filter(nums):
    return filter(lambda x: x%2==0, nums)

def multiply_by_three(nums):
    return map(lambda x: x*3, nums)

def convert_to_string(nums):
    return map(lambda x: 'The Number: %s' % x,  nums)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipeline = convert_to_string(
               multiply_by_three(
                   even_filter(nums)
               )
            )
for num in pipeline:
    print(num)


from functools import reduce

def pipeline_func(data, fns):
    return reduce(lambda a, x: x(a),
                  fns,
                  data)

pipeline_func(nums, [even_filter,
                     multiply_by_three,
                     convert_to_string])

# 感谢谢网友S142857 提供的shell风格的python pipeline
class Pipe(object):
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        def generator():
            for obj in other:
                if obj is not None:
                    yield self.func(obj)
        return generator()

@Pipe
def even_filter(num):
    return num if num % 2 == 0 else None

@Pipe
def multiply_by_three(num):
    return num*3

@Pipe
def convert_to_string(num):
    return 'The Number: %s' % num

@Pipe
def echo(item):
    print(item)
    return item

def force(sqs):
    for item in sqs: pass

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

force(nums | even_filter | multiply_by_three | convert_to_string | echo)

