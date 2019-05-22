#!/usr/bin/env python
# coding: utf-8

# # Python I: Extras
# 
# This extra material is intended for self study between the [Python I](../Python1/Python-1.html) and [Python II](../Python2/Python-2.html) workshops.  It should help you review and expand on the topics covered in Python I.
# 
# This material may also be a useful reference if you're already familiar with these ideas and want to learn about Python's syntax.
# 
# We'll do additional review at the start of Python II.
# 
# ## Contents
# 
# * [Review](#Review)
# 
# * [Data objects](#Data-Objects)
#     + [Dictionaries](#Dictionaries)
# 
#     + [Comprehensions](#List-and-Dictionary-Comprehensions)
# 
# * [Combining conditionals](#Combining-Conditionals)
# 
# * [Learn More](#Want-to-learn-more?)

# ## Review 
# 
# * Numeric types (`int`,`float`): 
# ```
# my_int=4
# ```
# * Strings (`str`): 
# ```
# my_string="cat"
# ```
# * Lists (`list`): 
# ```
# my_list=[my_int,my_string]
# ```
# * For loops:
# ```
# for k in range(10):
#     print(k)
# ```
# * Conditionals
# ```
# if my_string=="cat":
#     print("This is a cat!")
# else:
#     print("This is not a cat!")
# ```
# 
# <center>
# <h3>Review Exercises</h3>
# </center>
# 
# 1. Create a list, `exlist`, with at least two of each data type below:
#     * Numeric (Integer)
#     * String
#     * List
#     
# 2. Create empty lists and write a loop to sort `exlist` into three different lists: 
#     * `numlist`
#     * `strlist`
#     * `listlist` 
#     
#     by each element's type.  Remember that the `type` function can tell you what type each object is.
#     
# 3. Adapt your loop to work with the `test` loop below.

# In[1]:


test=["basin",78,["obtainable","public"],89,90,[],[10,20,30,40,50],"orange"]


# 4. Which element in the list `test` has the longest length?  (Check length with the `len` function.)

# ## Data Objects
# 
# In Python I, we introduced a number of important data structures in Python: string and numeric types, as well as lists.  We used indexing to specify particular parts of the sequential objects - strings and lists.  Here we introduce dictionaries, which provide a useful alternative format for some types of information.  List and dictionary comprehensions provide a more succinct way to generate lists and dictionaries. 
# 
# ### Dictionaries
# 
# Dictionaries provide a "mapping object"; instead of an index, they used named "keys" to organized data.  Dictionaries also benefit from faster performance than lists in most cases, due to their use of <a href="https://en.wikipedia.org/wiki/Hash_table">hash tables</a>.  
# 
# A dictionary is defined as follows:

# In[2]:


class_dict = {"course":"Python II","location":"Davis Library","time":"4pm"}
type(class_dict)


# In this case, `"course"`, `"location"`, and `"time"` serve as the "keys" for this dictionary.  Keys play a similar role to the indices we use for lists (or strings).  We can print a particular value by placing its key in the same square brackets `[]` used by list indices.

# In[3]:


print(class_dict["location"])


# A numeric index **will not** work with dictionaries.
# 
# We can also generate a list of all of the keys for a dictionary using the `.keys()` method. 

# In[4]:


print(class_dict.keys())


# ### List and Dictionary Comprehensions
# 
# Python provides some shortcuts to generating lists and dictionaries, especially those that you might (now) generate with a list.  For example, let's generate a list of the square of each number from 1 to 15.

# In[5]:


squares=[]
for n in range(1,16):
    squares.append(n**2)
print(squares)


# Using a "comprehension", we can shorten this to a single line, effectively bringing the loop inside the `[]` used to define the list.

# In[6]:


squares=[x**2 for x in range(1,16)]
print(squares)


# The same general format holds for defining dictionaries.

# In[7]:


squaresdict={k:k**2 for k in range(1,16)}
print(squaresdict)


# We can include conditional statements at the end of the comprehension to build more flexible comprehensions.

# In[8]:


sentence="the quick brown fox jumped over the lazy dog"
sentence=sentence.split(" ") #splits the string into a list with each space
print(sentence)
print([w for w in sentence if len(w)>4])


# <center>
# <h3>Exercises</h3>
# </center>
# 
# 1. Write a list comprehension to create a list of just the values (i.e. the squares) from `squaresdict`.
# 
# 2. Write a list comprehension with `os.listdir` to list all of the files in a directory that have a particular extension (e.g. end with .txt).  Try it against a folder in your computer with at least one such file.

# ## Combining Conditionals
# As our needs become more complex, we can combine conditions using Boolean Algebra operators `and` and `or`.

# In[9]:


num=5
letter="a"
(letter in ["a","b","c"]) and num<3 


# This is equivalent to using Boolean values directly:

# In[10]:


True and False


# In[11]:


#similarly...
(letter in ["a","b","c"]) or num<3 


# In[12]:


True or False


# Conditions can be grouped with parentheses, or negated with `not`)

# In[13]:


True or (False and False)


# In[14]:


(True or False) and not 5<3


# Remember, complex conditions can be simplified: 
# 
# `(True or False) and False` is equivalent to `True and False` since 
# 
# `(True or False)` evaluates to `True`.
# 
# <center>
# <h3> Exercise </h3>
# </center>
# 
# 1. Define `a` and `b` as conditions evaluating to True and False.  Write a line corresponding to exclusive or - it should retrun `True` if only one, but not both of `a` and `b` are `True`. Check your function against the built-in exclusive or operator, `^`.
# 
# ```
# a=True
# b=False
# # should return True
# a=False
# b=False
# # should return False
# ```

# ## Want to learn more?
# 
# The topics we've introduced are covered in significantly more depth in **[Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)**
# 
# * **[Chapter 1 - Python Basics](https://automatetheboringstuff.com/chapter1/)**
#   + Basic numeric and string variable types.  
#   + `print`, `len`, etc. 
#   + Basic user input.
# 
# * **[Chapter 2 - Flow Control](https://automatetheboringstuff.com/chapter2/)**
#   + Conditional statements
#   + Loops
# 
# * **[Chapter 4 - Lists](https://automatetheboringstuff.com/chapter4/)**
#   + Lists and indexing    
# 
# * **[Chapter 4 - Dictionaries](https://automatetheboringstuff.com/chapter5/)**
#   + Dictionaries, and how to use one to help make a basic tic-tac-toe game.
