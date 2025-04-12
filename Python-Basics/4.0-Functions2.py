# %%
#Check if a string is palindrome or not 
def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Hello"))

# %%
#Calculate the factorials of a number using recursion
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(6))

# %%
#A Function To Read A File and count the frequency of each word
def count_word_frequency(file_path):
    word_count={}
    with open(file_path,'r') as file:
        for line in file:
            words=line.split()
            for word in words:
                word=word.lower().strip('.,!?;:"\'')
                word_count[word]=word_count.get(word,0)+1
    
    return word_count

filepath='sample.txt'
word_frequency=count_word_frequency(filepath)
print(word_frequency)

# %%
#Validate email address

import re
# Email validation function
def is_valid_email(email):
    """This function checks if the email is valid."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Calling the function
print(is_valid_email("test@example.com"))  # Output: True
print(is_valid_email("invalid-email"))  # Output: False

# %% [markdown]
# ##### Lambda Functions in Python
# ##### Lambda functions are small anonymous functions defined using the **lambda** keyword. They can have any number of arguments but only one expression. They are commonly used for short operations or as arguments to higher-order functions.

# %%
#Syntax
lambda arguments: expression

# %%
def addition(a,b):
    return a+b

# %%
addition(2,3)

# %%
addition=lambda a,b:a+b
type(addition)
print(addition(5,6))

# %%
def even(num):
    if num%2==0:
        return True
    
even(24)

# %%
even1=lambda num:num%2==0
even1(12)

# %%
def addition(x,y,z):
    return x+y+z

addition(12,13,14)

# %%
addition1=lambda x,y,z:x+y+z
addition1(12,13,14)

# %%
## map()- applies a function to all items in a list
numbers=[1,2,3,4,5,6]
def square(number):
    return number**2

square(2)

# %%
list(map(lambda x:x**2,numbers))

# %% [markdown]
# #### The map() Function in Python
# The map() function applies a given function to all items in an input list (or any other iterable) and returns a map object (an iterator). This is particularly useful for transforming data in a list comprehensively.

# %%
def square(x):
    return x*x

square(10)

# %%
numbers=[1,2,3,4,5,6,7,8]

list(map(square,numbers))


# %%
## Lambda function with map
numbers=[1,2,3,4,5,6,7,8]
list(map(lambda x:x*x,numbers))

# %%
### MAp multiple iterables

numbers1=[1,2,3]
numbers2=[4,5,6]

added_numbers=list(map(lambda x,y:x+y,numbers1,numbers2))
print(added_numbers)

# %%
## map() to convert a list of strings to integers
# Use map to convert strings to integers
str_numbers = ['1', '2', '3', '4', '5']
int_numbers = list(map(int, str_numbers))

print(int_numbers)  # Output: [1, 2, 3, 4, 5]


# %%
words=['apple','banana','cherry']
upper_word=list(map(str.upper,words))
print(upper_word)

# %%
def get_name(person):
    return person['name']

people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33}
]
list(map(get_name,people))



# %% [markdown]
# #### Conclusion
# The map() function is a powerful tool for applying transformations to iterable data structures. It can be used with regular functions, lambda functions, and even multiple iterables, providing a versatile approach to data processing in Python. By understanding and utilizing map(), you can write more efficient and readable code.

# %% [markdown]
# ##### The filter() Function in Python
# The filter() function constructs an iterator from elements of an iterable for which a function returns true. It is used to filter out items from a list (or any other iterable) based on a condition.

# %%
def even(num):
    if num%2==0:
        return True

# %%
even(24)

# %%
lst=[1,2,3,4,5,6,7,8,9,10,11,12]

list(filter(even,lst))


# %%
## filter with a Lambda Function
numbers=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5,numbers))
print(greater_than_five)

# %%
## Filter with a lambda function and multiple conditions
numbers=[1,2,3,4,5,6,7,8,9]
even_and_greater_than_five=list(filter(lambda x:x>5 and x%2==0,numbers))
print(even_and_greater_than_five)

# %%
## Filter() to check if the age is greate than 25 in dictionaries
people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33},
    {'name':'John','age':25}
]

def age_greater_than_25(person):
    return person['age']>25

list(filter(age_greater_than_25,people))

# %% [markdown]
# ##### Conclusion
# The filter() function is a powerful tool for creating iterators that filter items out of an iterable based on a function. It is commonly used for data cleaning, filtering objects, and removing unwanted elements from lists. By mastering filter(), you can write more concise and efficient code for processing and manipulating collections in Python.


