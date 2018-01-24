# encoding: utf-8
"""
@version:3.6
@author:lamplight
@file:04.py
@time:2018/1/2119:21
工厂模式：
最常用的一种设计模式，在工厂模式中，
我们在创建对象时，不会对客户端暴露创建逻辑，
并且是通过用同一个共同的接口 来指向新创建的对象
"""
class GreekGetter(object):
    def __init__(self):
        self.tarns = dict(dog='awang', cat='amiao')

    def get(self, msigid):
        return self.tarns.get(msigid, str(msigid))

class EnglishGetter(object):
    def get(self, msgid):
        return str(msgid)

# 创建接口
def get_loaclizer(language='English'):
    languages = dict(English=EnglishGetter, Geek=GreekGetter)
    print(type(languages[language]()))
    return languages[language]()

e, g = get_loaclizer(language='English'), get_loaclizer(language='Geek')

print(e)

for msigid in 'dog parrot cat bear'.split():
    print(e.get(msigid), g.get(msigid))