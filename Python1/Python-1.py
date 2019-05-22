#!/usr/bin/env python
# coding: utf-8

# <center><h1>Python I: Beginner Basics</h1></center>
# 
# <center>Claire Cahoon, Matt Jansen, Nathan Kelber, and Kristina Bush</center>
# 
# <center>Thursday, May 23, 2019</center>

# **<font color=red>Note:</font>** 
# If you would like to use Python for the duration of this workshop without downloading anything (or have problems downloading Anaconda), we recommend using [pyfiddle.io](https://pyfiddle.io/).  Make sure you set Python version to 3.6 on the left side of the screen.
# 
# If you would like to save your work and continue to use Python on your computer, we recommend downloading Anaconda. 
# 
#    * Please install Anaconda following the instructions in [Setup](https://triangle-digital-humanities-institute.github.io/Python/Setup.html)  **before** the workshop if possible.
#    * If you haven't already installed Anaconda, please begin downloading the [Anaconda distribution of Python](https://www.anaconda.com/download/) as soon as possible.  It's a large download and can be slow to download over wifi.  If needed, we also have a limited number of thumb drives with the Anaconda installers.  Please flag one of the staff if you need to copy the installer.
# 
# 
# 
# 

# <center> <h1>Getting Started</h1> </center>
# 
# **Goals:**
# 
# * Get the Anaconda Distribution of Python 3.7 downloaded and installed on your computer
# * Learn to work with basic Python objects
# * Introduce Loops and Conditionals
# 
# ## Why Python?
# 
# Python is a general-purpose programming language that has become popular in a number of application areas.  Python can be easier to learn than some other languages because it emphasizes (human) readability and flexibility.  Python is [the third most used language on GitHub](https://octoverse.github.com/projects#languages); this popularity translates into a wide variety of packages (sets of functionality developed by other users) to apply Python to different problems and tasks.
# 
# If you haven't worked with a programming language before, learning Python will introduce you to approaches and thought processes common to many similar programming languages, making it easier to learn other languages.
# 
# ### Use Cases:
# 
# * Scripting: writing code to automate labor-intensive, repeptitive tasks.  For example, extracting text from thousands of pdf files and sorting them into directories based on the resulting text files.
# 
# * Quantitative analysis: specialized tools and functions for everything from fitting deep learning models with `tensorflow` to  creating interactive visualizations with `bokeh`.
# 
# * Natural Language Processing: extracting text from different file formats and parsing and analyzing sentiment using tools from the `NLTK` package.
# 
# * Web development, Image processing, Web scraping, Acessing APIs, and many more.
# 
# However, there are few things you can do in Python that can't also be done elsewhere!  If you already know one or more programming language, you'll have to decide where Python best fits or helps in your own workflows.
# 
# #### <font color=red>Warning!</font>
# 
# If you're already very comfortable with programming, you may find this workshop very simple.  Python II later in the day may be more helpful if you're already familiar with the concepts below and just need to learn new syntax, but both workshops will be focused on the basics.  You're welcome to stay, review, and help other attendees!
# 
# ####  Python 2 vs Python 3
# 
# Both Python 2 and Python 3 are widely used in research.  Unfortunately, while both Python 2 and 3 are very similar, there are a few key syntax differences. Python 3 was released in 2008; nearly all important tools have been re-written or updated for Python 3.  Python 2 will no longer be supported after 2020.  This workshop will focus on Python 3.
# 
# 
# 
# ## Integrated Development Environments (IDEs)
# 
# An IDE is software that groups together the many components needed to develop in a programming language, such as a code editor, compiler, and debugger, in a convenient interface. There are many different IDEs to choose from.
# 
# While not required, an IDE can make Python easier to use.  As you gain experience, you can choose whether an IDE is right for your uses and which one works best for you. For the purposes of this workshop, we will use the Spyder IDE, which comes packaged with Anaconda.
# 
# Open Spyder:
# * **Windows**: Start>Anaconda3 64-bit>Spyder
# * **Mac**: Applications>Anaconda Navigator>Spyder
# 
# ![SpyderIDE.png](https://github.com/UNC-Libraries-data/Python/raw/master/Python1/images/SpyderIDE.png)
# 
# Spyder's default interface provides three panes:
# 
# * The Editor pane (left) is a scripting window for writing Python code.
# * The Console pane (bottom right) contains a console for executing code.
# * The Explorer pane (top right) contains other helpful tools listing defined variables, files in the working directory, and other help.

# <center> <h1>1. Entering code</h1> </center>
# 
# We'll begin by using Python as a simple calculator.  
# 
# For the purposes of this workshop, Python code will be presented in numbered grey cells as below.  Any output generated will also be displayed.

# In[147]:


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

# In[148]:


3*3


# **Note:** We can annotate our code with comments.  Python uses `#` to denote comments.  Anything typed after a `#` will be ignored on execution of the code.

# In[149]:


#1+2
5/2 #division


# <center>
# <h3>Exercises</h3>
# </center>
# 
# 1. What is 126544 squared? (Exponentiation is denoted `**`)
# 
# 2. What is 5 divided by 0?

# <center> <h1>2. Variables</h1> </center>
# 
# We need Python to store various values and objects for future re-use. Python has many default data types available.  We will focus on a few common examples.
# 
# ## Strings and Numbers
# 
# We assign a value to a variable using `=`.  We do not need to declare a type or give any other information.

# In[150]:


text="Hello, World"
number=42


# String objects, like `text` above, contain textual values.  These are identified to Python by quotes; you can use either ' or " as long as you use the same type to begin and end your string. You can't do mathmatical operations on strings.
# 
# Python uses several different numeric data types for storing different values. Examples include integers, long integers, and floating point numbers (decimals).  Numbers can also be stored in string values using quotes.
# 
# For example:

# In[2]:


notnumber="42" #This is stored as text, not a number


# Once we have defined an object, we can use it again, most simply by printing it.

# In[152]:


print(text)


# **Note:** The print command is one of the most basic differences between Python 2 and Python 3. 
# In Python 2, print does not require parentheses:
# 
# `print text`
# 
# In Python 3, you must include parentheses:
# 
# `print(text)`
# 
# We can also modify the contents of variables in various ways, including redefining them or changing their type. In some cases this is crucial to how Python can work with them.  For example:

# In[153]:


print(number+58)
#print(number+notnumber)


# So we can add a value, 58, to our number object, but we can't add our notnumber object.  Let's double check what notnumber contains:

# In[154]:


print(notnumber)


# In[155]:


print(number)


# Even those these appear the same to our eye, Python uses them very differently.  Remember how we defined notnumber?  Let's check what data type Python is using with `type`.

# In[156]:


type(notnumber)


# Fortunately Python provides a set of *functions* to convert objects between different data types.  A function packages a set of prewritten commands to accomplish a particular task.  Most functions take one or more objects as inputs or 'arguments' and produce some new object as output.
# 
# The `int` function takes an object as an argument and converts it to an `int` (integer) numeric object.  The usage is as follows:

# In[157]:


newnumber=int(notnumber)
print(newnumber)
type(newnumber)


# `int` objects can only hold integer values (whole numbers).  If you have decimal values, use the `float` (floating decimal) type instead.

# In[158]:


myfloat=float(newnumber)+0.5
print(myfloat)


# Now we can try adding objects again.

# In[159]:


print(number+newnumber)


# ### Getting help with functions
# 
# You can access documentation for functions in Python with `help`, for example `help(sum)`.  Base Python functions and those provided by packages also usually have online documentation that may be easier to read.
# 
# <center>
# <h3>Exercises</h3>
# </center>
# 
# 1. Define two variables, `j` and `k` with values 37 and 52 respectively.
# 2. What is the sum of `j` and `k`? The product?  Write code for each of these in the editor window.
# 3. Now define `j` and `k` to be 8 and 3.  Re-use your code from the editor to determine their sum and product.
# 
# 
# ## Lists
# 
# Python's lists store objects in a sequence.  For example, we can save numbers and characters:

# In[160]:


my_list=[1,2,3,"four"]
print(my_list)


# We can also directly place previously defined objects into a list (even other lists!):

# In[5]:


obj0=12
obj1="cat"
obj2=["a","b","c"]
my_list1=[obj0,obj1,obj2]
print(my_list1)


# Once we've defined a list, we can add more elements to it with the `.append` function.

# In[6]:


my_list1.append("dog")
my_list1.append(42)
print(my_list1)


# <center>
# <h3>Exercise</h3>
# </center>
# 
# 1. Create a list that includes:
#      * your favorite color
#      * your two favorite holidays (as a list within the list)
#     
#     For example:
#     `["red",["Halloween","New Years"]]`
#     
# 2. Then append the number of pets you have as a new list item
#  
# 
# 
# ### Indexing
# 
# Python retains the order of elements in our list and uses that order to retrieve objects in lists.  These numbered positions are called indices.
# 
# We use `[` and `]` to contain indices.
# 
# Most importantly, **Python starts counting at zero**: The first element in your list is denoted `[0]`, the second `[1]`, the third `[2]` and so on.

# In[163]:


my_list2 = ["cat","dog","parrot"]
print(my_list2[2])


# We can use multiple indices for lists within lists, one after the other:

# In[164]:


#recall
my_list1=[12, 'cat', ['a', 'b', 'c']]
print(my_list1[2][1]) #i.e. the second element of the list held in the third element of my_list1


# The `len` function provides the length of an object in Python.

# In[165]:


print(len(my_list1))


# If `len(my_new_list)=10` that means there are ten elements in the list, so the indices are 0 through 9.  We can use the `range` function with `len` to generate a list of indices.

# In[166]:


my_indices1 = list(range(len(my_list1)))
print(my_indices1)


# #### Indexing beyond lists
# 
# Indexes can also be used with any sequential data type, which includes strings.
# 
# If you want to find a range of indexes, you can use two numbers with `:` in between. Note that Python does not stops at the index before the one you note as the end of the range.
# 
# For example:

# In[167]:


my_str="The quick brown fox jumps over the lazy dog."
print(my_str[4])
print(my_str[4:9]) #4:9 indicates characters 4-8


# We can also work from right to left using negative numbers.  Furthermore, using `:` ranges with one end blank will automatically go to the end of the object.

# In[168]:


print(my_str[-4:])
print(my_str[:4])


# We can still use multiple nested indices across sequential data types.  For instance, a list of strings:

# In[169]:


["home","away"][0][0:3]


# Unfortunately, not all data types are sequential - indices will not work on numeric values:  
# 
# <center>
# <h3>Exercises</h3>
# </center>
# 
# 1. Try to use indexing to get the tenth digit of `my_pi` as defined below.  Does it work as defined?  Do we need to change the variable somehow?
# ```
# my_pi=3.141592653589793
# ```
# 2. Below is a list of lists containing the NATO phonetic codes for each letter of the alphabet.  Each list within `nato` contains a letter of the alphabet and its corresponding code.
# ```
# nato=[["A","Alfa"],
#           ["B","Bravo"],
#           ["C","Charlie"],
#           ["D","Delta"],
#           ["E","Echo"],
#           ["F","Foxtrot"],
#           ["G","Golf"],
#           ["H","Hotel"],
#           ["I","India"],
#           ["J","Juliett"],
#           ["K","Kilo"],
#           ["L","Lima"],
#           ["M","Mike"],
#           ["N","November"],
#           ["O","Oscar"],
#           ["P","Papa"],
#           ["Q","Quebec"],
#           ["R","Romeo"],
#           ["S","Sierra"],
#           ["T","Tango"],
#           ["U","Uniform"],
#           ["V","Victor"],
#           ["W","Whiskey"],
#           ["X","X-ray"],
#           ["Y","Yankee"],
#           ["Z","Zulu"]]
# ```
# 
# * What is the fifteenth letter of the alphabet?
# * What is the code for the twenty-third letter of the alphabet?
# * What is the fourth letter of the code for the eighth letter of the alphabet?
# 
# There are several other important data types we won't cover today.  We will cover Python's data type for mapping between values, dictionaries, in Python II.
# 
# Read more about Python's built-in data types <a href=https://docs.python.org/3/library/stdtypes.html>here</a>.

# <center> <h1>3. Conditionals</h1> </center>
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

# In[170]:


num=5
num<3


# In[171]:


letter="a"
letter in ["a","b","c"]


# ## Conditional Statements
# 
# A conditional statement allows your code to branch and behave differently based on defined conditions.
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

# In[172]:


num=5
if num>4:
    print("This number is greater than four")


# In[173]:


num=3
if num>4:
    print("This number is greater than four")


# Adding `else` lets us give instructions if our condition is `False`.

# In[174]:


num=3
if num>4:
    print("This number is greater than than four")
else:
    print("This number is less than or equal to four")


# Finally, the `elif` command lets us split the possible values of `num` into more groups.

# In[175]:


num=8
if num<3:
    print("This number is less than three")
elif num<10:
    print("This number is greater than or equal to three and less than ten")
else:
    print("This number is greater than ten")


# <center>
# <h3>Exercise</h3>
# </center>
# 
# 1. Using indexing, write a conditional that print a word only if it ends with the letter 'e'.
# Template:
# ```
# testword=<your choice of word>
# if <condition using testword>:
#         print(testword)
# ```

# <center> <h1>4. Loops</h1> </center>
# 
# ## For Loops
# 
# A "for loop" allows us to apply the same steps to each element in a list or other iterable.  In essence, loops let us automate tasks relative to some sequence that we might *otherwise* write like this:

# In[182]:


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

# In[183]:


my_nums=list(range(6))

for n in my_nums:
    print(n)


# We can also loop within loops.  Indentation is key to control which blocks of code are executed within which loop.

# In[184]:


#Nesting loops - indentation is key!
newnato=[] #initialize an empty list
for index in range(5): #Loops 5 times
    total=0 #resets to zero each loop
    for entry in nato[index]: #loops through list items at index[index] in the nato list we used earlier 
        total=total+len(entry) #add up length of both strings in each entry
        #example: at index[0], this loop will go through "A" and then "Alpha," adding the length of each to the total
    new=[nato[index],total] #Create a list that includes the item from nato and the total
    newnato.append(new) #Append these lists to a larger list
print(newnato)


# Notice that before the loop begins we create an **empty list**.  This is a common stragegy to collect outputs from some or all of the loops iterations.  This can generalize to numbers by defining a zero-valued variable before the loop and modifying it with each iteration.

# ## For Loops with Conditionals
# 
# Loops become even more useful when combined with conditionals, to perform different steps based on each value in the loop.

# In[185]:


for number in range(10):
    if number % 2 == 0: # % denotes the modulo operation - the result is the remainder after dividing by 2
        print(number)


# Recall that we can combine multiple conditions with `and`.

# In[186]:


scores=[95,90,66,83,71,78,93,81,87,81]
grades=[]
for score in scores:
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"
    grades.append([score,grade])       
print(grades)


# **Exercise:**
# 1. Why do I only specify `score>=80` etc. in the `elif` statements?
# 2. How many numbers between 1 and 100 are divisible by 7?
# 3. Make a new list of NATO codes keeping only those that use the letter "a" in their code.

# ### <font color=blue>Breaks (Advanced)</font>
# 
# We can use the break statement with a conditional to stop the loop if a certain condition occurs.
# 
# First, lets get some new functions from a package called `random`.  
# * `from random import choices,seed` makes the functions `choices` and `seed` from the `random` package available in our Python session.
# * `choices(population=range(100),k=50)` will sample 50 random numbers (with replacement) from the numbers 0-99.  
# * `seed(1234)` locks the pseudo-random number generator so your results should match mine - try running this again without `seed`!
# 
# You can read more about the functions in the `random` package [here](https://docs.python.org/3/library/random.html).  We'll revisit packages next week!

# In[187]:


from random import choices,seed 

seed(1234)

test=choices(population=range(100),k=50)
print(test)


# In[188]:


total=0
for number in test:
    if number>10:
        total=total+number
    else:
        print("This number is too low:",number)
        break
print(total)


# What does the above loop do?  How would this run differently if we disabled the break by commenting (i.e. `#break`)?
# 
# <center>
# <h3><font color=blue>Exercise (Advanced)</font></h3>
# </center>
# 
# 1. Use the `choices` function above to generate a random list of 50 numbers in 0-99. Write a loop that will find the sum of only the first 6 even numbers.

# ## Next Up (Python II):
# * Reading and writing external files 
# * User-defined Functions
# * Loading Packages
# * Survey of useful packages for Data Analysis
#     + Pandas
# 
# ## Learn More:
# 
# If you'd like more practice, you can attempt our **[Python I: Extra](https://unc-libraries-data.github.io/Python/Extras/Python-1-Extras.html)**.
# 
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




