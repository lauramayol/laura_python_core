## Classes and OOP

- What is a class?
    A programmer defined type

- How do you define a new class called `MyFirstClass`?
    class MyFirstClass():

- How do you create an object of the class `MyFirstClass`?
    class MyFirstClass():
        def MyFirstObject(self):

- What is instantiation?
    Creating a new object.

- What are attributes?
    Assigning values to named elements of an object.

- What does it mean when an object is embedded?
    When an object is an attribute of another object.

- What is the difference between `copy.copy` and `copy.deepcopy`?
What do they each do?
    copy.copy : duplicates any object, but not its embedded objects if any
    copy.deepcopy: duplicates any object, including all of the embedded within.

- What is the difference between a pure function and a modifier?
    A pure function does not modify any of its objects, just returns something when it is called. A modifier will modify the objects that are passed via parameter.

- What is object-oriented programming?
    Writing code that is composed of objects and operations that do something with those objects to achieve the desired result.


## Methods

- What is a method?
    A function associated with a class.

- How is a method different than a function?
    Syntax is different and the method only exists in relationship to the class.

- What is invocation?
    Calling a method

- What is the `__init__` method and what is it used for?
    It initializes an object

- Give an example `__init__` method for a `Car` class with attributes:
`make`, `model` and `year`.

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.mode = model
        self.year = year

- How do `__init__` methods handle variable arguments?
    As long as default values are specified, the first value provided in the object call will be assigned to the first argument and so on. It cannot take more variables than number of arguments.

- What is the `__str__` method used for?
    It returns a string type and can be used to print your return value.

- How do you use a `__str__` method?
    You can use it as any other string variable.

- What is operator overloading?
    Changing the behavior of an operator so that it works with programmer defined types.

- What is an example of operator overloading?
    object.__format__ = it is called by the format() function


## TYPE-BASED DISPATCH?

- What is polymorphism?
    Functions that work with different types

- Why is polymorphism beneficial?
    Because you can use the same code on different types of objects.
