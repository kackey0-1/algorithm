def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapper


# add_numが実行される前にdecoratorが起動される
# print_infoの引数には"add_num"が渡される
@print_info
def add_num(a, b):
    return a + b


"""
f = print_info(add_num)
r = f(10, 20)
print(r)
"""
r = add_num(10, 20)
print(r)
