class CountedObject:
    
    counter = 0
    live_objects = 0
    
    def __init__(self):
        CountedObject.counter += 1
        CountedObject.live_objects += 1
        self.serial_number = CountedObject.counter

    def __del__(self):
        print(f"Object No. {self.serial_number} deleted")
        CountedObject.live_objects -= 1
    
    def num_allocated():
        return CountedObject.live_objects
    
obj1 = CountedObject()
obj2 = CountedObject()
print(f"Live objects: {CountedObject.num_allocated()}")
obj1 = None
print(f"Live objects: {CountedObject.num_allocated()}")