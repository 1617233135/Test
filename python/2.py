#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class student:
   '所有学生的基类'
   stu_count = 0
 
   def __init__(self, name, stu_no,stu_calss,male):
      self.name = name
      self.stu_no =stu_no
      self.stu_class=stu_class
      self.male=male
      student.stu_count += 1

   def displayStuInfo(self):
	print"student number:",self.male

   def displaycount(self):
       print"Count",Student.stu_count
       

      
