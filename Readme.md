# Python Mutable and Immutable

## Mutable Data Types
### List, Set, Dictionary, Bytearray, Array

## Immutable
### Integres , Floating-point numbers, Boolean, Strings, Tuples, Frozen set, Bytes.

#### If we create a variable and give a name to it like:
```python
username = "Kaushik"
```
So then memory create a reference object named Kaushik.
But then if we give another username:
```python
username = "Python"
```
Then Memory will create another object for this and then it become another name reference and then username points to this new object. So in this case, we can say that the string is immutable because we cannot change the value of the string, we can only create a new string and point to it.


# Data Types

- Numbers : Integers, Floating-point numbers, Complex numbers
- Sequences : Strings, Lists, Tuples
- Sets : Set, Frozen set
- Mappings : Dictionary
- Boolean : True, False
- Binary : Bytes, Bytearray, Memoryview
- Tuple : A tuple is an ordered collection of items that is immutable. It can contain elements of different data types. Tuples are defined using parentheses ().
```python
my_tuple = (1, "Hello", 3.14)
```
- List : A list is an ordered collection of items that is mutable. It can contain elements of different data types. Lists are defined using square brackets [].
```python
my_list = [1, "Hello", 3.14]
```
- Set : A set is an unordered collection of unique items that is mutable. Sets are defined using curly braces {}.
```python
my_set = {1, 2, 3, 4, 5}
```
- File: A file is a collection of data that is stored on a computer. It can be used to read and write data. Files are defined using the open() function.
```python
file = open("example.txt", "r")
```

- Boolean : A boolean is a data type that can have one of two values: True or False. Booleans are used to represent the truth value of an expression.

- Functions : A function is a block of code that performs a specific task. Functions are defined using the def keyword.
```python
def my_function():
    print("Hello, World!")
```
- Classes : A class is a blueprint for creating objects. It defines the properties and behaviors of the objects. Classes are defined using the class keyword.
```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")
```
- Advance: Decorators, Generators, Context Managers, Coroutines, Metaclasses, Descriptors, Iterators, and more. These are more advanced concepts in Python that are used for specific purposes and can be explored further as needed.

# List = Array
- A list is an ordered collection of items that is mutable. It can contain elements of different data types. Lists are defined using square brackets [].
```python
my_list = [1, "Hello", 3.14]
``` 

# Dictionary = Object
- A dictionary is an unordered collection of key-value pairs that is mutable. Dictionaries are defined using curly braces {}.
```python
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

