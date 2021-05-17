# Prototype design pattern is used when the concept of an existing
# object has to differ from that of the new object. This design
# pattern can quite efficiently copy the properties of an object
# to a different object without wasting much resources and time.
# It works by implementing different interfaces using a factory
# method to create and manage the interfaces. 

# Importing copy library which is required to create mutable copies
# of a given target object.
import copy

# Defining class prototype which will be used to clone exiting object
class Prototype:

   _type = None
   _value = None

   def clone(self): # method to clone object
      pass

   def getType(self): # method to get object's return type
      return self._type

   def getValue(self): # method to get values/parameters of the target object
      return self._value

# Creating classes to demonstrate prototype design pattern.
# The classes Type1 and Type2 are quite simple as they both have a 
# type and a value, and a function that is implementing the copy
# function to create the prototype
class Type1(Prototype):

   def __init__(self, number):
      self._type = "Type1"
      self._value = number

   def clone(self):
      return copy.copy(self)

class Type2(Prototype):

   """ Concrete prototype. """

   def __init__(self, number):
      self._type = "Type2"
      self._value = number

   def clone(self):
      return copy.copy(self)

# This class is used to create and manage prototypes
class ObjectFactory:

   # Manages prototypes.
   # Static factory, that encapsulates prototype
   # initialization and then allows instatiation
   # of the classes from these prototypes.
   

    # Creating 4 protoypes to clone different parameters of the original classes
   __type1Value1 = None
   __type1Value2 = None
   __type2Value1 = None
   __type2Value2 = None

    # Method to initialize prototype
   @staticmethod
   def initialize():
      ObjectFactory.__type1Value1 = Type1(1)
      ObjectFactory.__type1Value2 = Type1(2)
      ObjectFactory.__type2Value1 = Type2(1)
      ObjectFactory.__type2Value2 = Type2(2)

    # Methods to generate prototype using different parameters
   @staticmethod
   def getType1Value1():
      return ObjectFactory.__type1Value1.clone()

   @staticmethod
   def getType1Value2():
      return ObjectFactory.__type1Value2.clone()

   @staticmethod
   def getType2Value1():
      return ObjectFactory.__type2Value1.clone()

   @staticmethod
   def getType2Value2():
      return ObjectFactory.__type2Value2.clone()

# Main method
def main():
    # Calling factory method that handles the prototype creation
   ObjectFactory.initialize()
   
   # Displaying prototypes built using factory method
   instance = ObjectFactory.getType1Value1() # this instance creates a clone of Type1 with it's original value
   print("%s: %s" % (instance.getType(), instance.getValue()))
   
   instance = ObjectFactory.getType1Value2() # this instance creates a clone of Type1 with a different value
   print("%s: %s" % (instance.getType(), instance.getValue()))
   
   instance = ObjectFactory.getType2Value1() # this instance creates a clone of Type2 with a different value
   print("%s: %s" % (instance.getType(), instance.getValue()))
   
   instance = ObjectFactory.getType2Value2() # this instance creates a clone of Type2 with it's original value
   print("%s: %s" % (instance.getType(), instance.getValue()))

# Used to call the main function
if __name__ == "__main__":
   main()