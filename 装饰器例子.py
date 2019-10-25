def partial(fun,*args,**kwargs):
    def new_func(*fargs,**fkwargs):
        kwargs.update(fkwargs.copy())
        return fun(*args,*fargs,**kwargs)
    return new_func
def update(wrapper,fun1):
    wrapper.__name__ = fun1.__name__
    return wrapper
def wraps(fun):
    return partial(update,fun)
def dec(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('hello world')
        return func(*args,**kwargs)
    #update(wrapper,func)
    return wrapper
def fun2(a,b):
    return a+b
import functools
fun3 = functools.partial(fun2,3)
print(fun3(4))





