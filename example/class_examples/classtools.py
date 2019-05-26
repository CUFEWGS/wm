# -*- coding: utf-8 -*-
# @Time     : 2019/5/26 18:09
# Author    ：Wang Guosong
# @File     : classtools.py
# @Software : PyCharm

"Assorted class utilities and tools"


class AttrDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with class names and a name=value pair for
    each attribute stored on the instance itslef (but not attrs
    ingerited form its class). Can be mixed into any class,
    and will work on any instance.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ','.join(attrs)

    def __repr__(self):
        return '[%s：%s]' % (self.__class__.__name__, self.gatherAttrs())


if __name__ == '__main__':

    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)

# from example.class_examples.person import Person
# bob = Person('Bob Smith')
# list(bob.__dict__.keys())
# dir(bob)
# len(dir(bob))
# list(name for name in dir(bob) if not name.startswith('__'))
