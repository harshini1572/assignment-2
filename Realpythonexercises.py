#!/usr/bin/env python
# coding: utf-8

# In[4]:


# List containing the details of employees in an organization.

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]


# In[2]:


# A class dog is created ,(class is a blue print of an object.). class is defined by class keyword.
# pass is a class's body.

class Dog:
    pass


# In[3]:


# in the body of a class now the properties like age and name of a dog is given.
# The properties that all Dog objects are defined in a method called .__init__().
# first parameter will always be a variable called self. 
# self.name = name creates an attribute called name and assigns to it the value of the name parameter.
# self.age = age creates an attribute called age and assigns to it the value of the age parameter.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# In[5]:


# Now a class attribute is created,class attributes have same value for all class instances.
# following Dog class has a class attribute called species with the value "Canis familiaris":

class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# In[8]:


# it is IDLE's interactive window.
# This creates a new Dog class with no attributes or methods.

>>> class Dog:
...    pass


# In[9]:





# In[ ]:


# a new Dog object is created.
# new Dog object is at 0x106702d30 which is a memory address.

>>> Dog()
<__main__.Dog object at 0x106702d30


# In[ ]:


# another new dog object is created.
# The new Dog instance is located at a different memory address.

>>> Dog()
<__main__.Dog object at 0x0004ccc90>


# In[ ]:


# Here two new Dog objects are created and assigned them to the variables a and b.
# comparing a and b using the == operator, the result is False.

>>> a = Dog()
>>> b = Dog()
>>> a == b
False


# In[ ]:


# created a new Dog class with a class attribute called .species and two instance attributes called .name and .age:

>>> class Dog:
...     species = "Canis familiaris"
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age


# In[ ]:


# this is the error because here they didnot provided values for the name and age.

>>> Dog()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Dog()
TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'


# In[ ]:


# parmeters are given.
# This creates two new Dog instances—one for a nine-year-old dog named Buddy and one for a four-year-old dog named Miles.

>>> buddy = Dog("Buddy", 9)
>>> miles = Dog("Miles", 4)


# In[ ]:


# After creating the Dog instances, the instance attributes are accessed using dot notation.

>>> buddy.name
'Buddy'
>>> buddy.age
9

>>> miles.name
'Miles'
>>> miles.age
4


# In[ ]:


# class attributes are also accessed using dot notation.

>>> buddy.species
'Canis familiaris'


# In[ ]:


# Here in thi piece of code the attributes are changed dynamically.

>>> buddy.age = 10
>>> buddy.age
10

>>> miles.species = "Felis silvestris"
>>> miles.species
'Felis silvestris'


# In[ ]:


# Here Two instance methods are created.
# description() returns a string displaying the name and age of the dog.
# speak() has one parameter called sound and returns a string containing the dog’s name and the sound the dog makes.

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


# In[ ]:


# In this instance methods are seen in action by opening this in IDLE interactive shell.

>>> miles = Dog("Miles", 4)

>>> miles.description()
'Miles is 4 years old'

>>> miles.speak("Woof Woof")
'Miles says Woof Woof'

>>> miles.speak("Bow Wow")
'Miles says Bow Wow'


# In[ ]:


# created a list object. The list contains the names of three men.
# used print() to display a string

>>> names = ["Fletcher", "David", "Dan"]
>>> print(names)
['Fletcher', 'David', 'Dan']


# In[ ]:


# When you print(miles), geo a cryptic looking message telling that miles is a Dog object at the memory address 0x00aeff70. 

>>> print(miles)
<__main__.Dog object at 0x00aeff70>


# In[ ]:


# changed the name of the Dog class’s .description() method to .__str__():
class Dog:
    # Leave other parts of Dog class as-is

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"


# In[ ]:


# by print(miles), we got the output!


>>> miles = Dog("Miles", 4)
>>> print(miles)
'Miles is 4 years old'


# In[ ]:


# A Dog class is created with attributes : name,age,breed.

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


# In[ ]:


# Now we modeled the dog park by instantiating a bunch of different dogs in the interactive window

>>> miles = Dog("Miles", 4, "Jack Russell Terrier")
>>> buddy = Dog("Buddy", 9, "Dachshund")
>>> jack = Dog("Jack", 3, "Bulldog")
>>> jim = Dog("Jim", 5, "Bulldog")


# In[ ]:


# this contains the sounds of the Dogs.
buddy.speak("Yap")
'Buddy says Yap'

jim.speak("Woof")
'Jim says Woof'

jack.speak("Woof")
'Jack says Woof'


# In[ ]:


# created a child class for each of the three breeds called, Jack Russell Terrier, Dachshund, and Bulldog.

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# In[ ]:


# created a child class, and created new class with its own name and then put the name of the parent class in parentheses.

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


# In[ ]:


# With the child classes defined, we can now instantiate some dogs of specific breeds in the interactive window
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)


# In[ ]:


# Instances of child classes inherit all of the attributes and methods of the parent class:


>>> miles.species
'Canis familiaris'

>>> buddy.name
'Buddy'

>>> print(jack)
Jack is 3 years old

>>> jim.speak("Woof")
'Jim says Woof'


# In[ ]:


# It is to determine which class a given object belongs to.
type(miles)
<class '__main__.JackRussellTerrier'>


# In[ ]:


#  Here isinstance() takes two arguments, an object and a class. 
# In this, isinstance() checks if miles is an instance of the Dog class and returns True

>>> isinstance(miles, Dog)
True


# In[ ]:


# The miles, buddy, jack, and jim objects are all Dog instances
# but miles is not a Bulldog instance, and jack is not a Dachshund instance
>>> isinstance(miles, Bulldog)
False

>>> isinstance(jack, Dachshund)
False


# In[ ]:


# JackRussellTerrier class is created.
# Now .speak() is defined on the JackRussellTerrier class with the default argument for sound set to "Arf".

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


# In[ ]:


# save and run the file. You can now call .speak() on a JackRussellTerrier instance without passing an argument to sound.
miles = JackRussellTerrier("Miles", 4)
miles.speak()
'Miles says Arf'


# In[10]:


#  in the editor window, change the string returned by .speak() in the Dog class.
class Dog:
    # Leave other attributes and methods as they are

    # Change the string returned by .speak()
    def speak(self, sound):
        return f"{self.name} barks: {sound}"


# In[11]:


# Now, creating a new Bulldog instance named jim, jim.speak() returns the new string.
jim = Bulldog("Jim", 5)
jim.speak("Woof")
'Jim barks: Woof'


# In[ ]:


# .speak() on a JackRussellTerrier instance won’t show the new style of output.
miles = JackRussellTerrier("Miles", 4)
miles.speak()
'Miles says Arf'


# In[ ]:


# accessing the parent class from inside a method of a child class by using super()

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


# In[ ]:


# Updating dog.py with the new JackRussellTerrier class. 

>>> miles = JackRussellTerrier("Miles", 4)
>>> miles.speak()
'Miles barks: Arf'


# In[ ]:




