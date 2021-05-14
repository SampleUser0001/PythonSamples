# -*- coding: utf-8 -*-

class SuperClass:
  """ Sample Class """

  def __init__(self):
    self.name = ""
  
  def setName(self, name):
    self.name = name

  def printHello(self):
    if self.name == "":
      print('Who are you?')
    else: 
      print('Hello! ' + self.name + '!')


class SubClass(SuperClass):
  def __init__(self):
    super().__init__()
    
  def get_name(self):
    return self.name

  def printHello(self):
    super().printHello()
    print('I am SubClass!')
