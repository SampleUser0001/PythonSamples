# -*- encoding: utf-8 -*-
import sys
sys.path.append('./')
import MyClass

a = MyClass.MyClass()
a.printHello()

a.setName('Hoge')
a.printHello()