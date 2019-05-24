import timeit

def append(alist, iterable):
    for item in iterable:
        alist.append(item)

def extend(alist, iterable):
    alist.extend(iterable)

def append_one(a_list, element):
    a_list.append(element)

def extend_one(a_list, element):
    """creating a new list is semantically the most direct
    way to create an iterable to give to extend"""
    a_list.extend([element])

def append_loop(foo, reps):
    for i in range(reps):
        foo.append(i)

def append_comp(foo, reps):
    [foo.append(i) for i in range(reps)]

def extend_lst(foo, reps):
    foo.extend([i for i in range(reps)])

def extend_tup(foo, reps):
    foo.extend((i for i in range(reps)))

if __name__ == '__main__':
    print(min(timeit.repeat(lambda: append([], "abcdefghijklmnopqrstuvwxyz"))))
    # 1.7087784369999994
    print(min(timeit.repeat(lambda: extend([], "abcdefghijklmnopqrstuvwxyz"))))
    # 0.47141181200000126

    print(min(timeit.repeat(lambda: append_one([], 0))))
    # 0.2082819009956438
    print(min(timeit.repeat(lambda: extend_one([], 0))))
    # 0.239701926009729

    repetitions = 600

    print(timeit.timeit('append_loop([], repetitions)', setup='from __main__ import append_loop, repetitions'))
    print(timeit.timeit('append_comp([], repetitions)', setup='from __main__ import append_comp, repetitions'))
    print(timeit.timeit('extend_lst([], repetitions)', setup='from __main__ import extend_lst, repetitions'))
    print(timeit.timeit('extend_tup([], repetitions)', setup='from __main__ import extend_tup, repetitions'))
