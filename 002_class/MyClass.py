# -*- encoding: utf-8 -*-

class MyClass:
    """ Sample Class """
    counter = 0;

    def __init__(self):
        MyClass.counter += 1
        self.name = ""
    
    def setName(self, name):
        self.name = name

    def printHello(self):
        if self.name == "":
            print('Who are you?')
        else: 
            print('Hello! ' + self.name + '!')

