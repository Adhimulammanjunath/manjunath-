''
# !or
# c = 0
# for val in set1,set2:
# c=c+1
# if c==1:


s1= "Hello how are you"
s2="Hello how is"
s1=s1.split(" ")
s2=s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)




# ! find the 8th fibanochi number
 #num = 8
 # n1 = 0
 # n2 =  1

 
 # for val in range(run0:
 # ans =n1 +n2
 # n1 = n2
 # n2 = ans
 # print(ans)
 

# find the 8th fibanochi number
num=8
n1=0
n2=1

for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
print(ans)

 # ! constructors
 # ? Eg:?
 # * unparametarised constructor
#  class profile:
 #  def _init_(self):
# print('hello world")

# obj_profile:
obJ_init_()


# ? EG:3
#*  parameterised constructor
# class profile :
# def_init_(self, id, name, age):
# print(id, name, age)
#print(id,name, age)
# obj = profile(1, "sid", 29)

# ? Eg:4
class c1:
    name = "sid"
    place = "cbe"
    
    def m1(self):
        name = "sid"       


 # eg:6
# to use the variables inside the constructor in another methods
class class1:
    def __init__(self):
        self.name = "manju"
        self.email = "manju@gmail.com"
        # return name, email # error --> cannot use return with constructor

    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()


# ! -------> inheritance

# the process of utilisng the method and attributes of parent class
 # throught the objects of child class it is called as inheritances


# 5 types of inheritances
# single inheritances
# multilevel inheritances
#multiple inheritances
# hybrid inheritances
# heirarichal  inheritances



# * single inheritances
# ? it has only one parent class and only one child class
# | Eg:1
class parent:
    def m1(self):
        print("I am parent class")


class child(parent):
    def m2(self):
        print("I am child class")

obj = child()
obj.m1()

# ! eg:2
# class c1:
#    def_init_(self):
     #   print("Iam  constructor from parent class")
     
    #    class child1(c1):
    #        pass

    
    #    obj = child1()




# ! Eg:3
# class parent:
  #  name = "manju"

  # class child(parent):
      #  name = "name1"

      #  def display(self):
         #   print(self.name)

         #   d =child()
          #  d.disply()



# ! Eg:2

class c1:
    def __init__(self):
        print("Iam constructor from parent class")

class child1(c1):
    pass

obj = child1()



# ! multilevel inheritnce
# ? Eg:1
# class voice:
  #   def sound(self):
    #    print("all th animals have their own voice")

# class cat(voice):
  #  def dog_voice(self):
     #   print("meow")

      #  class parrot(cat):
         #   def parrot_voice(self):
            #   print("meow")


              #  class parrot(cat):
                #    def parrot_voice(self):
               #         print("speak")

# all = parrot()
# all.dog_voice()
# all.cat_voice()
# all.sound()
# all.parrot-voice()


# ! multilevel inheritance
# ? eg:1
class voice:
    def sound(self):
        print("all animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("meow")

class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()                       
                     
              

# ! Multilevel inheritance
# ? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")
        
class cat(dog):
    def cat_voice(self):
        print("Meow")
        
class parrot(cat):
    def dog_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()



# Multiple Inheritance
 #? It has multiple parent and 1 child
class while_pertol:
    def function_w(self):
        print("used to Airplans")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol(while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
p=petrol()
p.defanition()
p.function_o()


honda = Honda()
honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, "Hatchback")




# ! Multiple Inheritance
# ? it has multiple paremt and 1 child

class while_petrol:
    def function_w(self):
        print("used to Airplane")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")

class petrol(while_petrol, Organic_petrol, premium_petrol):
    def defanition(self):
print("Petrols types")
p=petrol()
p.defanition()
p.function()
''    
# ! Eg:2
class addition:
    def add(self, a,b):
        print(a+b)

class substract:
    def sub(self, a,b):
        print(a-b)

class multiply:
    def mul (self, a,b):
        print(a*b)

class division(addition, substraction, multiply):
    def div(self, a, b):
        print(a/b)

calc = division()
calc.add(3, 4)
calc.mul(5, 2)           
