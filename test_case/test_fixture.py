import pytest

'''
socpe表示作用域范围，从小到大
function ：每个用例被运行之前会被执行一次
class ：每个类被运行之前会被执行一次
module ：每个模块被运行之前会被执行一次
session ：项目启动时会被运行一次
'''



class Test111():
    def test_aa(self):
        print(111)
    def test_bb(self):
        print(111)

class Test222():
    def test_aa(self):
        print(11)
    def test_bb(self):
        print(111)
