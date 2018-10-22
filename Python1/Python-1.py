#!/usr/bin/env python
# coding: utf-8

# # Python I
# 
# [*Matt Jansen, Davis Library Research Hub*](https://guides.lib.unc.edu/mattjansen)
# 
# October 23, 2018

# **<font color=red>Note:</font>** Please begin downloading the [Anaconda distribution of Python](https://www.anaconda.com/download/) as soon as you can.  It's a large download and can be somewhat slow with a large number of attendees downloading at the same time over wifi.  If needed, we also have a limited number of thumb drives with the Anaconda installers.  Please flag one of the staff if you need to copy the installer.
# 
# ** Goals:**
# 
# * Get the Anaconda Distribution of Python 3.7 downloaded and installed on your computer
# * Learn the types of projects Python can help you with
# * Learn how to write and execute basic Python code with Spyder
# 
# # 0. Installing Python
# 
# If you use macOS or Linux, then you most likely already have Python on your computer!  Python does not come with Windows, but it may be on your machine if you have certain software installed.
# 
# ### Why not work with an existing installation?
# 
# Unless you've worked with Python already, your pre-existing installation may only include the bare minimum and may be an out of date version.  Therefore, we recommend installing a distribution, with Python and many useful add-ons.
# 
# ## Anaconda distribution
# 
# Anaconda packages the current version of Python 2 or 3 with over 150 packages included in the installation and hundreds of other supported.  This includes many of the most heavily used packages supporting data transformation and analysis, and software to manage and add new packages.
# 
# [Read more here](https://docs.anaconda.com/anaconda/packages/pkg-docs)
#     
# [Download Anaconda Here](https://www.anaconda.com/download/)
# 
# Download Python 3.7, 64-bit.
# 
# ![Download](https://github.com/UNC-Libraries-data/Python/raw/master/Python1/images/Conda_dl.png)
# 
# ####  PATH Variables and Default Installation
# 
# In most cases, it is best to leave the default settings for installation. 
# 
# 
# * If you are installing Python for the first time, select "Register Anaconda as the system Python"
# 
# ![Anaconda_install_settings.png](https://github.com/UNC-Libraries-data/Python/raw/master/Python1/images/Anaconda_install_settings.png)
# 
# * If you have Python-dependent software (e.g. ArcGIS, CAD software, etc), do not check "Register Anaconda as the system Python" or it may cause issues with your other programs.
#     + If you're unsure, open your PC's Command Line (Start>Windows System>Command Prompt) or Mac's Terminal (Applications>Utilities>Terminal) and type `python` and press Enter.  If you already have Python you should see something like the image below - do not check Register Anaconda as the system Python.
# ![Command Prompt Python](https://github.com/UNC-Libraries-data/Python/raw/master/Python1/images/Test_CMD.png)
# 
# 
# ####  Python 2 vs Python 3
# 
# Both Python 2 and Python 3 are widely used in research.  Unfortunately, while both Python 2 and 3 are very similar, they are not completely compatible.  Python 3 was released in 2008, and as of 2017 nearly all important tools had been re-written or updated for Python 3.  Python 2 will no longer be supported after 2020.  This workshop will focus on Python 3.
# 
# ### Anaconda Alternative - Pyfiddle
# 
# If you have problems installing Anaconda, you can also follow along today with [pyfiddle.io](https://pyfiddle.io/).  Make sure you set Python version to 3.6 on the left side of the screen.
# 
# ## Integrated Development Environments (IDEs)
# 
# While not required, an IDE can make Python easier to use.  As you gain experience, you can choose whether an IDE is right for your uses.  For the purposes of this workshop, we will use the Spyder IDE, which comes packaged with Anaconda.
# 
# ![SpyderIDE.png](https://github.com/UNC-Libraries-data/Python/raw/master/Python1/images/SpyderIDE.png)
# 
# Spyder's default interface provides three panes:
# 
# * The Editor pane (left) is a scripting window for writing Python code.
# * The Console pane (bottom right) contains a console for executing code.
# * The Explorer pane (top right) contains other helpful tools listing defined variables, files in the working directory, and other help.
# 
# 

# # 1. Entering code
# 
# We'll begin by using Python as a simple calculator.  
# 
# For the purposes of this workshop, Python code will be presented in numbered grey cells as below.  Any output generated will also be displayed.

# In[53]:


2+2


# To execute this in Spyder, copy or type the code yourself into the Ipython console pane. Press `Enter` to execute.
# 
# ![2+2_console.png](https://github.com/UNC-Libraries-data/Python/raw/master/Python1/images/2+2_console.png)
# 
# Alternatively, you can enter code into the Editor pane.  This is particularly useful when writing more complicated or reusable code.  The code you write in the Editor pane will be saved as a .py file to run or revise later. 
# 
# To use the Editor pane to save and execute code, type the code in the Editor pane, highlight the line(s) you want to execute and click:
# 
# * Run > Run Selection or Current Line
# * **Shortcut:**  **F9** (or **FN+F9** on many laptops)
# 
# The code will then execute in the Console pane.
# 
# Standard arithmetic operations are available in Python.

# In[54]:


3*3


# **Note:** We can annotate our code with comments.  Python uses `#` to denote comments.  Anything typed after a `#` will be ignored on execution of the code.

# In[59]:


#1+2
5/2 #division


# **Exercises**
# 
# 1. What is 126544 squared? (Note: exponentiation is denoted `**`)
# 
# 2. What is 5 divided by 0?
# 
# 3. Does Python follow the usual order of operations (PEMDAS)?

# # 2. Variables
# 
# Ultimately, we need Python to store various values and objects for future re-use. Python has many default data types available.  We will focus on a few common examples.
# 
# ## Strings and Numbers
# 
# We assign a value to a variable using `=`.  We do not need to declare a type or give any other information.

# In[60]:


text="Hello, World"
number=42


# String objects, like `text` above, contain textual values.  These are identified to Python by quotes; you can use either ' or " as long as you use the same type to begin and end your string.
# 
# Python uses several different numeric data types for storing different values. Examples include integers, long integers, and floating point numbers (decimals).  Numbers can also be stored in string values using double quotes.
# 
# For example:

# In[61]:


notnumber="42"


# Once we have defined an object, we can use it again, most simply by printing it.

# In[62]:


print(text)


# **Note:** The print command is one of the most basic differences between Python 2 and Python 3. In Python 2, print does require parentheses:
# 
# `print text`
# 
# We can also modify the contents of objects in various ways such as redefining them or changing their type. In some cases this is crucial to how Python can work with them.  For example:

# In[63]:


print(number+58)
#print(number+notnumber)


# So we can add a value, 58, to our number object, but we can't add our notnumber object.  Let's double check what notnumber contains:

# In[64]:


print(notnumber)


# In[65]:


print(number)


# Even those these appear the same to our eye, Python uses them very differently.  Remember how we defined notnumber?  Let's check what data type Python is using with `type`.

# In[66]:


type(notnumber)


# Fortunately Python provides a set of *functions* to convert objects between different data types.  A function packages a set of prewritten commands to accomplish a particular task.  Most functions take one or more objects as inputs or 'arguments' and produce some new object as output.
# 
# The `int` function takes an object as an argument and converts it to an `int` (integer) numeric object.  The usage is as follows:

# In[67]:


newnumber=int(notnumber)
print(newnumber)
type(newnumber)


# `int` objects can only hold integer values.  If you have decimal values, use the `float` (floating decimal) type instead.

# In[68]:


myfloat=float(newnumber)+0.5
print(myfloat)


# Now we can try adding objects again.

# In[69]:


print(number+newnumber)


# **Exercise**
# 1. Define two variables, `j` and `k` with values 37 and 52 respectively.
# 2. What is the sum of `j` and `k`? The product?  Write code for each of these in the editor window.
# 3. Now define `j` and `k` to be 8 and 3.  Re-use your code from the editor to determine their sum and product.
# 
# ## Lists
# 
# Python's lists store objects in a sequence.  For example, we can save numbers and characters:

# In[70]:


my_list=[1,2,3,"four"]
print(my_list)


# We can also directly place previously defined objects into a list (even other lists!):

# In[71]:


obj0=12
obj1="cat"
obj2=["a","b","c"]
my_list1=[obj0,obj1,obj2]
print(my_list1)


# Once we've defined a list, we can add more elements to it with the `.append` function.

# In[72]:


my_list1.append("dog")
print(my_list1)


# **Exercise** 
# 
# Create a list of:
#  * your favorite color
#  * your two favorite holidays (as a list within the list)
# 
# ### Indexing
# 
# Python retains the order of elements in our list and uses that order to retrieve objects in lists.  These numbered positions are called indices.
# 
# We use `[` and `]` to contain indices.
# 
# ** Most importantly, ** Python starts counting at **zero**.  So confusingly, the first element in your list is denoted `[0]`, the second `[1]`, the third `[2]` and so on.

# In[73]:


my_list2 = ["cat","dog","parrot"]
print(my_list2[2])


# We can use multiple indices for lists within lists, one after the other:

# In[74]:


#recall
my_list1=[12, 'cat', ['a', 'b', 'c']]
print(my_list1[2][1]) #i.e. the second element of the list held in the third element of my_list1


# The `len` function provides the length of an object in Python.

# In[75]:


print(len(my_list1))


# If `len(my_new_list)=10` that means there are ten elements in the list, so the indices are 0 through 9.  We can use the `range` function with `len` to generate a list of indices.

# In[76]:


my_indices1 = list(range(len(my_list1)))
print(my_indices1)


# #### Indexing beyond lists
# 
# Indexes can also be used with any sequential data type, which includes strings.
# 
# For example:

# In[77]:


my_str="The quick brown fox jumps over the lazy dog."
print(my_str[4])
print(my_str[4:9]) #4:9 indicates characters 4-8


# We can also work from right to left using negative numbers.  Furthermore, using `:` ranges with one end blank will automatically go to the end of the object.

# In[78]:


print(my_str[-4:])
print(my_str[:4])


# We can still use multiple nested indices across sequential data types.  For instance, a list of strings:

# In[79]:


["home","away"][0][0:3]


# Unfortunately, not all data types are sequential, so indices will not work with them. This includes numbers.  
# 
# **Exercise**
# 
# 1. Try to use indexing to get the tenth digit of `my_pi` as defined below

# In[80]:


my_pi=3.141592653589793


# 2. Can you think of a way we could change pi to make indexing work on it?

# 3. Below is a list of lists containing the NATO phonetic codes for each letter of the alphabet.  Each list within `nato` contains a letter of the alphabet and its corresponding code.

# In[81]:


nato=[["A","Alfa"],
      ["B","Bravo"],
      ["C","Charlie"],
      ["D","Delta"],
      ["E","Echo"],
      ["F","Foxtrot"],
      ["G","Golf"],
      ["H","Hotel"],
      ["I","India"],
      ["J","Juliett"],
      ["K","Kilo"],
      ["L","Lima"],
      ["M","Mike"],
      ["N","November"],
      ["O","Oscar"],
      ["P","Papa"],
      ["Q","Quebec"],
      ["R","Romeo"],
      ["S","Sierra"],
      ["T","Tango"],
      ["U","Uniform"],
      ["V","Victor"],
      ["W","Whiskey"],
      ["X","X-ray"],
      ["Y","Yankee"],
      ["Z","Zulu"]]


# * What is the fifteenth letter of the alphabet?
# * What is the code for the twenty-third letter of the alphabet?
# * What is the fourth letter of the code for the eighth letter of the alphabet?

# There are several other important data types we won't cover today.  We will cover Python's data type for mapping between values, dictionaries, in Python II.
# 
# Read more about Python's built-in data types <a href=https://docs.python.org/3/library/stdtypes.html>here</a>.
# 
# # 3. Conditionals
# 
# ## Conditions and Booleans
# 
# Conditionals allow for more flexible instructions, letting our code react differently as our inputs change.
# 
# Conditions often arise from comparisons:
# 
#         <          strictly less than
#         <= 	    less than or equal
#         > 	     strictly greater than
#         >= 	    greater than or equal
#         == 	    equal
#         != 	    not equal
#         is 	    object identity
#         is not 	negated object identity
#         in 	    sequence membership
#         not in 	sequence non-membership
# 
# **Note:** `=` is used for assignment, whereas `==` checks if two objects are equal.
# 
# Each condition considered evaluates to a Boolean value - `True` or `False`.

# In[11]:


num=5
num<3


# In[10]:


letter="a"
letter in ["a","b","c"]


# ## Conditional Statements
# 
# A conditional statement allows your code to branch and behave differently based on these conditions.
# 
# A simple conditional statement takes the form:
# 
# ```
# if <condition>:
#     <do something only if condition1 is true>
# ```
# 
# Your instructions can be as long as necessary, provided they remain indented.  Indentation is very important in Python as it groups lines of code without using explict characters like `{` and `}` as in many other language.  You can indent with spaces or tabs, but you must be **consistent**.
#  
# We can supply alternate steps if the condition is false with `else`, or even consider multiple conditions with `elif` (i.e. else if).
# 
# ```
# if <condition1>:
#     <do something if condition1 is true>
# elif <condition2>:
#     <do a different thing if condition1 is false and condition2 is true>
# else
#     <do a third thing if neither condition is true>
# ```

# In[8]:


num=5
if num>4:
    print("This number is greater than four")


# In[7]:


num=3
if num>4:
    print("This number is greater than four")


# Adding `else` lets us give instructions if our condition is `False`.

# In[13]:


num=3
if num>4:
    print("This number is greater than than four")
else:
    print("This number is less than or equal to four")


# Finally, the `elif` command lets us split the possible values of `num` into more groups.

# In[17]:


num=8
if num<3:
    print("This number is less than three")
elif num<10:
    print("This number is greater than or equal to three and less than ten")
else:
    print("This number is greater than ten")


# ## Compound Conditions
# 
# As our needs become more complex, we can combine conditions using Boolean Algebra operators `and` and `or`.

# In[5]:


num=5
letter="a"
(letter in ["a","b","c"]) and num<3 


# This is equivalent to using Boolean values directly:

# In[55]:


True and False


# Similarly:

# In[6]:


(letter in ["a","b","c"]) or num<3 


# In[56]:


True or False


# Conditions can be grouped with 

# In[57]:


True or (False and False)


# In[58]:


(True or False) and False


# Remember, complex conditions can be simplified: `(True or False) and False` is equivalent to `True and False` since `(True or False)` evaluates to `True`.
# 
# Conditions become far more powerful, when combined with Loops.

# # 4. Loops 
# 
# ## For Loops
# 
# A "for loop" allows us to apply the same steps to each element in a list or other iterable.  In essence, loops let us automate tasks relative to some sequence that we might otherwise write like this:

# In[82]:


sales=[5,2,7,9,3]
total_sales=0
total_sales=total_sales+sales[0]
total_sales=total_sales+sales[1]
total_sales=total_sales+sales[2]
total_sales=total_sales+sales[3]
total_sales=total_sales+sales[4]
print(total_sales)


# Loops take the form:
# 
# 
# `for <name> in <list>:`
# 
#         do something based on name
#         
#     
# * `<name>` is **completely arbitrary**, though i,j,k, and n are relatively common
# * `<list>` is a pre-defined list or other iterable object.
# * **Reminder: Indentation is very important in Python and must be used consistently across the loop(s)** Only the code indented under the loop will be run in each iteration.

# In[83]:


my_nums=list(range(6))

for n in my_nums:
    print(n)


# We can also loop within loops.  Indentation is key to control which blocks of code are executed within which loop.

# In[84]:


#Nesting loops - indentation is key!
newnato=[] #initialize an empty list
for index in range(5):
    total=0 #resets to zero each loop
    for entry in nato[index]:
        total=total+len(entry) #add up length of both strings in each entry
    new=[nato[index],total]
    newnato.append(new)
print(newnato)


# ## While Loops
# 
# The while loop behaves a little differently, though it has a similar format, using `while` instead of `for`.  Instead of looping through a pre-defined set, a while loop continues running until a certain condition is no longer true.

# In[85]:


a=0
while a<5:
    a=a+1
    print(a)


# Because there isn't a pre-defined end to a while loop, they can also be dangerous to your code!  If you aren't careful your while loop can go on forever.  A trivial example uses `while True:`.

# In[86]:


#Warning: this will run forever...
#while True:
#    print("oops")


# If you run something like this, or need to stop code currently executing for any reason, you can either:
#  * Press the red square at the top corner of the console window in Spyder
#  * Press CTRL+c

# ## Loops with Conditionals
# 
# Loops become even more useful when combined with conditionals, to perform different steps based on each value in the loop.

# In[18]:


for number in range(10):
    if number % 2 == 0: # % denotes the modulo operation - the result is the remainder after dividing by 2
        print(number)


# Recall that we can combine multiple conditions with `and`.

# In[14]:


scores=[95,90,66,83,71,78,93,81,87,81]
grades=[]
for score in scores:
    if score<80 and score>=70:
        grade="C"
    elif score>=90:
        grade="A"
    elif score<90 and score>=80:
        grade="B"
    elif score<70 and score>=60:
        grade="D"
    else:
        grade="F"
    grades.append([score,grade])       
print(grades)


# ** Exercise: **
# 1. How could I change the `for scores in scores` loop above to no longer need the `and` statements?  (Remember how `elif` works!).
# 2. How many numbers between 1 and 100 are divisible by 7?
# 3. Make a new list of NATO codes keeping only those that use the letter "a" in their code.

# ## Next Up (Python II):
# * Reading and writing external files 
# * Saving and executing .py scripts outside Spyder
# * Dictionaries
# * Comprehensions
# * User-defined Functions
# * Error handling with Try and Except
# * Survey of useful packages for Data Analysis
# 
# ## Questions?
# 
# If you're planning to attend Python II next week, please feel free to share any ideas or topics you'd like to see covered.  
# 
# You can also share ideas while filling out our [**Feedback Survey**](unc.libsurveys.com/davishubfeedback).
# 
# I'm available for one-on-one consultations on Python if you need help.  [Contact me here.](http://guides.lib.unc.edu/mattjansen)
# 
# Thanks for coming!

# ## References and Resources
# 
# * <a href="https://automatetheboringstuff.com/">Automate the Boring Stuff with Python</a>
# 
# * <a href="https://stackoverflow.com/questions/tagged/python-3.x?sort=frequent&pageSize=15">Stack Overflow</a>
# 
# * <a href="https://www.google.com/">Google!</a>
# 
# * <a href="http://www.karsdorp.io/python-course/">Python Programming for the Humanities</a>

# In[ ]:




