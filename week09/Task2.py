def new_map(func, args):
    result = []
    for i in args:
        result.append(func(i))
    yield result

list1 = [1,2,3,4,5]
list2 = new_map(lambda x:x*x, list1)
print(list(list2))