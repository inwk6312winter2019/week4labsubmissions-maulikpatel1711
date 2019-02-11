class Point():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def distance(self):
        return int(self.a) - int(self.b)

a= input("Enter value for a:")
b =input("Enter value for b:")
myobj = Point(a,b)
print("Distance: ",myobj.distance())

