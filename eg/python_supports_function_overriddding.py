# Overriding is the
# property
# of
# a
#
#
# class to change the implementation of a method provided by one of its base classes.
#
#
# Overriding is a
# very
# important
# part
# of
# OOP
# since
# it
# makes
# inheritance
# utilize
# its
# full
# power.By
# using
# method
# overriding
# a
#
#
# class may "copy" another class, avoiding duplicated code, and at the same time enhance or customize part of it.Method overriding is thus a part of the inheritance mechanism.
#
#
# In
# Python
# method
# overriding
# occurs
# by
# simply
# defining in the
# child
#
#
# class a method with the same name of a method in the parent class.When you  define a method in the object you make this latter able to satisfy that  method call, so the implementations of its ancestors do not come in play.
#
#
# class Parent(object):
#     def __init__(self):
#         self.value = 4
#
#     def get_value(self):
#         return self.value
#
#
# class Child(Parent):
#     def get_value(self):
#         return self.value + 1
#
#
# Now
# Child
# objects
# behave
# differently
#
# >> > c = Child()
# >> > c.get_value()
# 5