#Understarnding Python Data Types
# 1. Python Numeric Data Type
# Holds Numeric values
# a. int: holds signed integers of non-limited length
# b. float: holds floating decimal points upto 15 d.p.
# c. complex: Complex numbers are written with a "j" as the imaginary part:

#Python List Data Type
# A list is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ].
languages = ["python", "ruby", "java"]
print(languages)
# Access List Items
print(languages[0])

# Python Tuple Data Type
# A tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.
products = ('XBox', 456.890, 'Brave', 34)
print(products)
#Accessing Tuple elements
print(products[3])

# Python String Data Type
#
# String is a sequence of characters represented by either single or double quotes
name = "Favour"
print(f"My girlfriend's name is {name}")

# Python Set Data Type
#
# The Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }. For example,
employee_id = {234,456, 906, 245, 897}
print(employee_id)

# Python Dictionary Data Type
#
# Python dictionary is an ordered collection of items. It stores elements in key/value pairs.
girl_age = {"Favour": 19, "Cate": 22, "Linet": 21}
print(girl_age)