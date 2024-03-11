#1. Sum of Integers in a List:
# Accept user input to create a list of integers
user_input = input("Enter a list of integers: ")
integer_list = [int(x) for x in user_input.split()]

# Compute the sum of all integers in the list
sum_of_integers = sum(integer_list)

print("Sum of integers:", sum_of_integers)
print("\n")

#2. Print Book Names Using a For Loop:
# Create a tuple containing the names of five favorite books
favorite_books = ("To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby", "The Catcher in the Rye")

# Use a for loop to print each book name on a separate line
for book in favorite_books:
    print(book)
print("\n")

#3. Dictionary with User Input:
# Use a dictionary to store information about a person
person_info = {}

# Ask the user for input
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary
print("Person Information:", person_info)
print("\n")

#4. Intersection of Sets:
# Accept user input to create two sets of integers
setA = set(map(int, input("Enter elements for setA: ").split()))
setB = set(map(int, input("Enter elements for setB: ").split()))

# Create a new set containing only the elements that are common to both sets
common_elements = setA.intersection(setB)

# Print the result
print("Common elements:", common_elements)
print("\n")

#5. List Comprehension for Words with Odd Number of Characters:
# Store a list of words
word_list = ["apple", "banana", "orange", "grape", "kiwi"]

# Use list comprehension to create a new list with words having an odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

# Print the result
print("Words with odd number of characters:", odd_length_words)
