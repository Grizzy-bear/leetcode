# encoding: utf-8
"""
@version:3.6
@author:lamplight
@file:02.py
@time:2018/1/2118:15
共享模式：brog
一个能在实例之间共享状态的单例模式，单例模式涉及到一个单一的类，
该类福贼创建自己的对象，同时确保只有 单个对象  被创建，
这个类提供了一种访问其唯一的对象的方式，这样就能直接访问，
不需要初始化该类的对象。
"""
class Borg(object):
    """pirate attr"""
    _share_state = {}

    def __init__(self):
        """__dict__ 存储信息"""
        self.__dict__ = self._share_state
        self.state = 'init'

    def __str__(self):
        return self.state

class YourBorg(Borg):
    pass

if __name__ == '__main__':
    """init 2 classes"""
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1:{0}'.format(rm1))
    print('rm1:{0}'.format(rm2))
