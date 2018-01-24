# encoding: utf-8
"""
@version:3.6
@author:lamplight
@file:01.py
@time:2018/1/2117:50
抽象工厂：
     抽象工厂模式是围绕一个超级工厂创建其他的工厂，该超级工厂有成为其他工厂的工厂，
这种类型的设计模式属于 创建形模式，他提供了一种创建对象的最佳方式
在抽象工厂模式中，接口只负责一个相关对象的工厂，不需要显示指定他们的类。
每个生成的工厂都能够 按照工厂模式提供对象
主要解决了： 接口选择的问题
使用场景举例：qq换肤程序， 一整套平台一起换肤，生成不同操作系统的皮肤程序
"""
import random

class PetShop(object):
    """super fctory"""
    def __init__(self, animal_fctory=None):
        self.pet_fctory = animal_fctory

    def show_pet(self):
        pet = self.pet_fctory.get_pet()
        print('we have a lovely {}'.format(pet))
        print('it will say:{}'.format(pet.speak()))
        print('we also have {}'.format(self.pet_fctory.get_food()))

class Dog(object):
    def speak(self):
        return 'woof'
    def __str__(self):
        return  'Dog'

class Cat(object):
    def speak(self):
        return 'meow'
    def __str__(self):
        return "Cat"

"""fctory"""
class DogFctory(object):
    def get_pet(self):
        return Dog()
    def get_food(self):
        return 'dog food'

class CatFactory(object):
    def get_pet(self):
        return Cat()
    def get_food(self):
        return 'cat food'

def choose_factory():
    return random.choice([DogFctory, CatFactory])()
shop = PetShop(choose_factory())
shop.show_pet()