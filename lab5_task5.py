class Point():
    def __init__(self, a = 1 ,b = 2):
        self.a = a
        self.b = b
    def __str__(self):
        return "str method:" + str(self.a) + " " + str(self.b)

    def add(self):
        print("Addtion is:" + str(int(self.a) + int(self.b)))

myobj = Point(1,2)
print(myobj)
myobj.add()

