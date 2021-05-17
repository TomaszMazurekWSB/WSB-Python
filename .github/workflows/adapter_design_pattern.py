# This is a demo code for Adapter design pattern. This design
# pattern is used when we are required to join two incompatible interfaces.
# It basically uses the concept of polymorphism to convert the interface
# of a class into another interface based on requirement.

# Creating the first interface
class EuropeanSocketInterface:
   def voltage(self): pass

   def live(self): pass
   def neutral(self): pass
   def earth(self): pass

# Adaptee implementing the first interface
class Socket(EuropeanSocketInterface):
   def voltage(self):
      return 230
   def live(self):
      return 1
   
   def neutral(self):
      return -1
   
   def earth(self):
      return 0

# Target interface which is normally incompatible with the
# first interface (i.e. EuropeanSocketInterface)
class USASocketInterface:
   def voltage(self): pass
   def live(self): pass
   def neutral(self): pass

# The Adapter, which implements the target interface
class Adapter(USASocketInterface):
   __socket = None
   def __init__(self, socket):
      self.__socket = socket
   
   def voltage(self):
      return 110
   
   def live(self):
      return self.__socket.live()
   
   def neutral(self):
      return self.__socket.neutral()

# Client class which requires the connection between adapter
# and adaptee to properly function
class ElectricKettle:
   __power = None
   
   def __init__(self, power):
	   self.__power = power
   
   def boil(self):
      if self.__power.voltage() > 110:
         print("Kettle on fire!")
      else:
         if self.__power.live() == 1 and \
            self.__power.neutral() == -1:
            print("Coffee time!")
         else:
            print("No power.")

# Main function
# In this implementation the adapter relies on the object implementation.
def main():
   # Initializing plugins
   socket = Socket()
   adapter = Adapter(socket) # Creating a bridge between the two incompatible interfaces
   kettle = ElectricKettle(adapter) # utilizing the interfaces
	
   # Running the function to checif bridge is successfully working or not
   kettle.boil()
	
   return 0

# Used to call the main method	
if __name__ == "__main__":
   main()