# -*- coding: utf-8 -*-
from sample import SuperClass, SubClass

if __name__ == '__main__':
  sub_class = SubClass()
  sub_class.setName('Hoge')
  sub_class.printHello()
  print(sub_class.get_name())
  