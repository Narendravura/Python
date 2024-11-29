#dictionaries
dict1={"name":"narendra"}
print(dict1)
dict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict2["brand"])

child1={
    "name":"narndra",
    "age":20
}
child2={
    "name":"narndra kumar",
    "age":21
}
child3={
    "name":"narndra vura",
    "age":22
}
children={
    "child1":child1,
    "child2":child2,
    "child3":child3,
}
print(children["child1"]["age"])

child1["address"]="hyderabad"
print(child1)#adding new key and value to dict
#looping of dict
for x in children:
    print(children[x])

for x, y in child1.items():
  print(x, y)

#if-else statements
a=22
b=25
if a<=25 :
   print("a is smaller than 25")
elif a == b:
  print("a and b are equal")

#looping concepts
while a<25:
   print(a)
   a=a+2
else:
   print("a  greater than 25")

mobiles_id=[25,23,252]
for x in mobiles_id:
   if x==250 :
        print(x)
        break
else:
   print ("number is not avaliable")


#functions

def my_func(fname):
   print (fname)
my_func("narendra")
my_func("kalyan")

y=lambda a,b:a*b*30
print(y(5,6))

#class and object
class Narendra:
    def vehicles(self):
      print("hero")

    def vehicle2(self):
      print('honda')


veh1=Narendra()
veh2=Narendra()
veh1.vehicles()
veh2.vehicle2()

class Car:
    def __init__(self,brand,model) :
      self.brand=brand
      self.model=model
    def display_info(self):
       print(f"this car is a {self.model} of {self.brand}")
kalyan_car=Car("Toyota", "Corolla")
kalyan_car.display_info()
#Iterator
fruit_prices={"apple":3,"banana":1,"cherry":5}
key_iterator=iter (fruit_prices)
while True:
    try:
      key=next(key_iterator)
      print(f"{key}:${fruit_prices[key]}")
    except StopIteration:
       break


#Polymorphism
class Electronics :
    def __init__(self,brand,model):
      self.brand=brand
      self.model=model
    def android_version(self):
       print("oreo")
class Mobile(Electronics):
    pass
class Tab(Electronics):
    def android_version(self):
       print("lollipop")
class Laptop(Electronics):
    def android_version(self):
       print("Windows")     
mobile1=Mobile("mi","note14")
tab1=Tab("apple","ipad")
laptop1=Laptop("asus","tuf15")
for x in (mobile1, tab1, laptop1):
  print(x.brand)
  print(x.model)
  x.android_version()


#Datetime
import datetime
x = datetime.datetime(2018, 9, 1)
print(x.strftime("%A"))

#math package
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x ,y) 

#python Json
import json
z={
   "name":"narendra",
   "age":"25",
   "vehicle":True,
   "bikes":("honda","hero"),
   "plane":None,
   "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(z))

#Error Handling
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#lambda Expressions
X=lambda A:A+10
print(X(5))

Y=lambda B:B*(22/7)
print(Y(6))