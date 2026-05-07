# script.py
def greet():
   print("Hello from greet!")
if __name__ == "__main__":
   print("This script is running directly!")
   greet()
   
"""The if __name__ == "__main__" construct in Python is used to determine whether a script is being run directly or imported as a module.
It ensures that certain code blocks execute only when the script is run directly, not when it is imported into another script."""

# in simple we use this so that we can run the code directly without doing and import  


# when we import this script in another script the code inside if __name__ == "__main__": will not run

"""Why Use It?

Prevent Unintended Execution: Ensures that code meant for standalone execution (e.g., tests, demos) does not run when the module is imported.

Reusable Modules: Allows Python files to act as both reusable modules and standalone scripts."""



'''The __init__ method in Python is a special method (also known as a constructor) that is automatically called when an object of a class is created. It is used to initialize the attributes of the object and set up its initial state. Here's why we use it:
Purpose of __init__

Object Initialization: It allows you to assign values to the object's attributes when the object is created.
Custom Setup: You can perform any setup or configuration needed for the object during its creation.
Encapsulation: It ensures that the object's data is encapsulated and initialized properly, making the class reusable and organized.
Example Explanation
'''

class Example:
   def __init__(self, data):
      self.data = data  # Assign the passed value to the object's attribute

# Creating an object of the class
obj = Example("Hello, World!")

# Accessing the object's attribute
print(obj.data)  # Output: Hello, World!

'''
self: Refers to the instance of the class. It allows you to access and modify the attributes of the specific object being created.
data: This is a parameter passed to the __init__ method. It allows you to provide custom values when creating an object.

Why Use It?
Without __init__, you would need to manually set attributes after creating an object, which is less efficient and error-prone. For example:'''
class Example:
    pass

obj = Example()
obj.data = "Hello, World!"  # Manually setting the attribute
print(obj.data)  # Output: Hello, World!


'''
Using __init__ simplifies this process by combining object creation and initialization into one step.
'''

