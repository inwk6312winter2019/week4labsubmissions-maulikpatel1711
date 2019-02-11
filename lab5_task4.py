from time import gmtime, strftime
from datetime import datetime,timedelta
# print("Current Time is:",strftime("%H:%M:%S", gmtime()))

class Time():
    def __init__(self,s1,s2):
         self.s1 = s1
         self.s2 = s2

    def is_after(self):
         return self.s1 < self.s2

y = datetime.now() - timedelta(days=1)
z = datetime.now()
print(y)
print(z)
myobj = Time(z,y)
print(myobj.is_after())

