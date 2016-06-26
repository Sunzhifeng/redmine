"""
    This moudle define some useful decorator for our app.
"""

import time


def timing(func):
    """ a timing decorator is used to count function running time.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print '<%s> took %s to run' % (func.__name__, str(end - start))

    return wrapper


def timing_all_class_method(Cls):
    """ a class decorator of timing method's time cost.
    """
    class NewCls(object):
        def __init__(self, *args, **kwargs):
            self.obj = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x

            x = self.obj.__getattribute__(s)
            if type(x) == type(self.__init__):    # x is instance method
                return timing(x)    # compute run time of method x
            else:
                return x

    return NewCls


@timing
def hello(content):
    print 'hello %s' % content


@timing_all_class_method
class Foo(object):
    def hello(self, content):
        print 'Foo:hello %s' % content


def main():
    hello('world')
    foo = Foo()
    foo.hello('world')


if __name__ == '__main__':
    main()
