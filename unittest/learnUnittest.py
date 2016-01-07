# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中unitest的案例
import unittest
import  testclass

# 测试模块中的函数
class mytestFunction(unittest.TestCase):
  ##初始化工作
  def setUp(self):
    pass
  #退出清理工作
  def tearDown(self):
    pass
  #具体的测试用例，一定要以test开头
  def testsum(self):
    self.assertEqual(testclass.sum(1, 2), 2, 'test sum fail')
  def testsub(self):
    self.assertEqual(testclass.sub(2, 1), 1, 'test sub fail')

#测试模块类中的函数
class mytestClass(unittest.TestCase):
  ##初始化工作
  def setUp(self):
    self.tclass = testclass.myclass()
    ##实例化了被测试模块中的类
  #退出清理工作
  def tearDown(self):
    pass
  #具体的测试用例，一定要以test开头
  def testsum(self):
    self.assertEqual(self.tclass.sum(1, 2), 3,  'test myclass.sum fail')
  def testsub(self):
    self.assertEqual(testclass.sub(2, 1), 1, 'test myclass.sub fail')

if __name__ =='__main__':
  unittest.main()