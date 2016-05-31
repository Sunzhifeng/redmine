import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print 'call %s ' % func.__name__
        return func(*args, **kwargs)
    return wrapper

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print '%s %s' % (text, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log
def now():
    print '2016-05-31'

@log2('execute')
def now2():
    print '2016-05-31'

if __name__ == '__main__':
    now()
    now2()

