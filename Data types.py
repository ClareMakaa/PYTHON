#Python Numeric Data type
num1 = 5
print(num1, "is of type", type(num1))
num2 = 2.0
print(num2, "is of type", type(num2))
num3 = 1+2j
print(num3, "is of type", type(num3))
print("\n")

#Python List Data Type [], elements and size can be changed/mutable
languages = ["Swift", "Jave", "Python"] #Can mix any data types in List
print(languages[0]) #indexing
print(languages[2])
print("\n")

#Python Tuple Data Type (), elements and size can't be changed/immutable
languages = ("English", "French", "Swahili")
print(type(("English", "French", "Swahili")))
print(languages[0]) #indexing
print(languages[2])
print("\n")

#Python String Data Type - immutable
title = "PLP Academy"
message ="Python for beginners"
print(message)
print(len(message))
print(message[0]) #Indexing
print(message[-1]) #Negative Indexing
print(message[0:6]) #Slicing
print (title == message) #Compare Two Strings
print(message + " and Professionals") #Concatenation
print(message * 4) #Repetition
print("\n")

#Python Set Data Type - A set is a collection of unique data.
empty_set = set() #Empty set
student_id ={112, 114, 116, 118} #sets are unordered, mutable collections
print(student_id)
student_id.add(122) #Add Items to a Set in Python
print(student_id)
removedValue = student_id.discard(122) #Remove an Element from a Set
print(student_id)
print("\n")

#Python Dictionary Data Type
empty_dictionary ={}
#Python dictionary is an ordered collection of items. It stores elements in key:value pairs.
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome","England": "London"}
print(capital_city)
#Keys are 'Nepal', 'Italy', 'England'
#Values are 'Kathmandu', 'Rome', 'London'
print(capital_city.keys())
print(capital_city.values ())
print(capital_city["England"])
print(capital_city["Italy"])
numbers = {1:"one", 2:"Two", 3:"Three"}
print("Initial numbers: ", numbers)
numbers[4]="Four" #Add Elements to a Python Dictionary
print("Updated numbers: ", numbers)
del numbers[4] #Change Value of Dictionary
print("Updated numbers: ", numbers)