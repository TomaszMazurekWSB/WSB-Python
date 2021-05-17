# Bridge Design pattern is used to join specific and independent
# abstractions, it is used when we have to implement platform 
# independent features or when different abstractions are required
# to be implemented for the same abstraction.
# In this example have a Cuboid class having three attributes
# named as length, breadth, and height and three
# methods named as produceWithAPIOne(), produceWithAPItwo(),
# and expand(). Our purpose is to separate out implementation
# specific abstraction from implementation-independent
# abstraction
  
# This is a specific API or abstraction which is used to produce cuboid
class ProducingAPI1:
  
    def produceCuboid(self, length, breadth, height):
  
        print(f'API1 is producing Cuboid with length = {length}, '
              f' Breadth = {breadth} and Height = {height}')
  
# This is a specific API or abstraction which is used to produce cuboid
class ProducingAPI2:
  
    def produceCuboid(self, length, breadth, height):
  
        print(f'API2 is producing Cuboid with length = {length}, '
              f' Breadth = {breadth} and Height = {height}')
  
# This is the class that has an independent and specific abstrraction implemented,
# namely expand() and produce().
class Cuboid:
  
    def __init__(self, length, breadth, height, producingAPI):
  
        # Initializing the necessarry variables
        self._length = length
        self._breadth = breadth
        self._height = height

        # Initializing the API to implement specific abstraction
        self._producingAPI = producingAPI
   
   # This a specific abstraction implementaion
    def produce(self):
  
        self._producingAPI.produceCuboid(self._length, self._breadth, self._height) # This acts as the bridge method to implement bridge design pattern
  
   # This is a independent method which is to be connected to the specific abstraction
    def expand(self, times):
       # Exapanding the generated cuboid
        self._length = self._length * times
        self._breadth = self._breadth * times
        self._height = self._height * times
  
# Main method
def main():
   # Initializing Cuboid object by passing values to the parameters, and the API to be used
   cuboid1 = Cuboid(1, 2, 3, ProducingAPI1())
   cuboid1.produce() # Using specific abstraction implementation to connect with independent method
  
   cuboid2 = Cuboid(19, 19, 19, ProducingAPI2())
   cuboid2.produce()

# Used to call the main function
if __name__ == "__main__":
   main()
