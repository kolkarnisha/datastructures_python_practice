"""Python functions, constructors, and the self parameter.

1. Creating and calling a normal function
------------------------------------------
Use ``def`` to create a function. Call it by writing its name followed by
parentheses and any required arguments.
"""


def greet(name):
		"""Print a greeting for the supplied name."""
		print(f"Hello, {name}!")


greet("Nisha")


def add_numbers(first, second):
		"""Return the sum of two numbers."""
		return first + second


result = add_numbers(10, 5)
print(result)  # 15


"""
2. Class, constructor, and self
-------------------------------
``__init__`` is the initializer that runs automatically when an object is
created. It is commonly called the constructor.

``self`` refers to the current object. It lets each object store and use its
own data, such as ``self.name`` and ``self.age``.
"""


class Student:
		def __init__(self, name, age):
				self.name = name
				self.age = age

		def introduce(self):
				print(f"My name is {self.name}. I am {self.age} years old.")


# Creating an object automatically calls __init__.
student_one = Student("Nisha", 20)

# Python automatically passes student_one as self.
student_one.introduce()

# This is the equivalent call, but the first form is preferred.
Student.introduce(student_one)


"""
Important points
----------------
* ``def`` creates a function.
* Calling ``greet("Nisha")`` runs the function.
* ``return`` sends a value back to the caller.
* ``__init__`` initializes a newly created object.
* ``self`` is the current object and must be the first parameter of an
	instance method.
* Do not pass ``self`` manually when calling ``student_one.introduce()``;
	Python passes it automatically.
"""
