#Python Numeric Data type
num1 = 5
print(num1, "is of type", type(num1))
num2 = 2.0
print(num2, "is of type", type(num2))
num3 = 1+2j
print(num3, "is of type", type(num3))

#Python List Data Type [], elements and size can be changed/mutable
languages = ["Swift", "Jave", "Python"] #Can mix any data types in List
print(languages[0]) #indexing
print(languages[2])

#Python Tuple Data Type (), elements and size can't be changed/immutable
languages = ("English", "French", "Swahili")
print(type(("English", "French", "Swahili")))
print(languages[0]) #indexing
print(languages[2])

#Python String Data Type
message ="Python for beginners"
print(message)
print(message[0]) #Slicing
print(message[0:6])
print(message + " and Professionals") #Concatenation
print(message * 4) #Repetition

#Python Set Data Type
student_id ={112, 114, 116, 118} #sets are unordered collections
print(student_id)

#Python Dictionary Data Type
#Python dictionary is an ordered collection of items. It stores elements in key:value pairs.
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome","England": "London"}
print(capital_city)
#Keys are 'Nepal', 'Italy', 'England'
#Values are 'Kathmandu', 'Rome', 'London'
print(capital_city.keys())
print(capital_city.values ())
print(capital_city["England"])
print(capital_city["Italy"])