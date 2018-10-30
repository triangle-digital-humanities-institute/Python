#!/usr/bin/env python
# coding: utf-8

# # Python II
# 
# [*Matt Jansen, Davis Library Research Hub*](https://guides.lib.unc.edu/mattjansen)
# 
# October 30, 2018
# 
# **Abstract:**
# This workshop will:
# * Briefly review the basics covered in Python 1
# * Learn how to work with files and directory
# * Introduce dictionaries
# * Survey some of the more important data-related packages

# ### NOTE:
# This workshop assumes that you already have the <a href="https://www.anaconda.com/download/">Anaconda distribution</a> of Python 3.7 installed.  Detailed installation instructions are available in the [Python I materials](https://unc-libraries-data.github.io/Python/Python1/Python-1.html). 
# 
# # Review
# 
# Last week, we introduced:
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
# 
# # Pseudocode
# 
# As you get started coding in Python, there will be many many tasks and steps you aren't familiar with!  As you learn new functions and approaches, you'll become better and better at searching for help online and reviewing documentation.  Learning to write and use pseudocode where appropriate can help organize your plan for any individual script.
# 
# Pseudocode is essentially a first draft of your code, written in English for **human consumption**, though with the tools of your programming language in mind.  For example, we might write pseudocode for extracting text from pdf files as:
# 
#     1. Set Working Directory (tell the computer where we've saved our files)
#     2. Loop through each pdf in the directory:
#         * open the pdf file
#         * extract text
#         * check length of text extracted
#             * if length is zero: add to problems list
#             * otherwise, add to output file
#     3. Write output file(s)
# 
# This process can divide a complicated task into more digestible parts.  You may not know how to open a pdf file or extract text from it, but you'll often have better luck finding existing help online on smaller tasks like these than with your overall goal or project.
# 
# <center>
# <h3>Exercises</h3>
# </center>
# 
# * Write pseudocode to summarize the following code:

# In[51]:


random_words=["statement", "toy", "cars", "shoes", "ear", "busy", 
              "magnificent", "brainy", "healthy", "narrow", "join", 
              "decay", "dashing", "river", "gather", "stop", "satisfying", 
              "holistic", "reply", "steady", "event", "house", "amused", 
              "soak", "increase"]

vowels=["a","e","i","o","u","y"]

output=[]

for word in random_words:
    count=0
    for char in word:
        if char in vowels:
            count=count+1
    if count>=3:
        output.append([word,count])


# * Write pseudocode to check an arbitrary list of numbers, `my_numbers`, to find all even numbers and convert them to odd numbers by adding one.  Put the resulting numbers into a new list `my_numbers2`.  (Recall `for` loops ,`if` conditions, and the modulo function `%` from Python 1.)
# 
# # Comments
# 
# Recall that Python ignores anything following a `#` as a comment.  Comments are a vital part of your code, as they leave notes about how or why you're doing something.  As you gain experience, you'll use comments in different ways.
# 
# Comments can also provide a link between pseudocode and real code.  Once you've written your pseudocode, use comments to put the major steps into your code file itself.  Then fill in the gaps with actual code as you figure it out.
# 
# Here's a possible answer to the previous exercise.

# In[52]:


#1. Get or define the list my_numbers
my_numbers=list(range(100))

#2. Create an empty list for the new all-odd numbers, called my_numbers2.

#3. Use a loop to iterate through the list of numbers

    #3a. For a given number check to see if it is even.
    
    #3b. If the number is even, add 1.
    
    #3c. Append the resulting number to the my_numbers2 list.


# <center>
# <h3>Exercise</h3>
# </center>
# 
# * Use your own pseudocode or the example above as an outline to fill in with Python code.  Test your code with the `my_numbers` object defined above.

# # Reading and Writing Files from Python
# 
# ## Packages
# 
# ### Installation
# 
# Packages provide additional tools and functions not present in base Python.  Python includes a number of packages to start with, and others can be installed using `pip install <package name>` and/or `conda install <package name>` commands **in your terminal**. 
# 
# Open your terminal by:
# * (PC) Start > Anaconda3(64-bit) > Anaconda Prompt
# * (Mac) Finder > Applications > Anaconda Navigator > Environments Tab > (play button listed next to "root") > Open Terminal
# 
# ### Loading
# 
# Once you've installed a package, you can load it into your current Python session with the `import` function.  Otherwise these functions will not be available.

# In[53]:


import os #functions for working with your operating system


# ## Working Directories
# 
# To open a file with Python, you'll need to tell your computer where it's located on your computer.  You can specify the entire absolute filepath (starting with C:\ on PC or / on Mac), or you can set a working directory and work with relative file paths. 
# 
# You can determine where a file is located on your computer by:
# 
# * (PC) Navigate to your desired folder in Windows Explorer and click on it.  Click in the address bar at the top of the window to copy the path.
# * (Mac) Right-click a file in your desired directory > Click Get Info > Highlight and copy the path listed next to "Where:"
# 
# If a file is located in your working directory, its relative path is just the name of the file!

# In[54]:


myfile="C:/Users/mtjansen/Desktop/Python/Python2/Python_Sales/day1.txt" #absolute path
os.path.isfile(myfile) #check if Python can find my file 


# #### Windows Paths
# Windows filepaths use `\`, which Python interprets as *escape characters*.  This can be fixed in several ways:
# 1. Replace `\` with `/`.
# 2. Replace `\` with `\\`.
# 3. Preface your path with `r`: 
# ```
#         r"C:\Users\mtjansen\Desktop"
# ```

# In[55]:


os.chdir("C:/Users/mtjansen/Desktop/Python/Python2/Python_Sales") #set working directory
myfile="day1.txt" #relative path
os.path.isfile(myfile)


# We can get a list of all files in the working directory with `os.listdir(".")`.

# In[56]:


print(os.listdir("."))
print(os.listdir("C:/Users/mtjansen/Desktop/Python/Python2/Python_Sales")) #alternatively we can specify a folder


# <center>
# <h3>Exercise</h3>
# </center>
# 
# * Download the zipped data availalble [here](https://github.com/UNC-Libraries-data/Python/raw/master/Python2/Python_Sales/Python_Sales.zip). Unzip them somewhere on your computer.
# 
# * Use `import os` and `os.chdir` to set your working directory to the unzipped folder "Python Sales".  Use `os.listdir` to check what files are stored there.
# 
# 
# ## Reading and Writing Files
# 
# Python requires you both open and close files explicitly.  If you forget to close a file, it can remain in use, preventing you from opening it later.
# 
# Best practices for reading and writing files use the `with` function to make sure files are automatically closed.

# In[57]:


with open('Day1.txt',"r") as txtfile: #"r" indicates that we are reading the textfile and not writing to it
    raw=txtfile.read() #read() retrieves raw text information from the file opened in txtfile
    
print(raw)


# In[58]:


rawlist=raw.splitlines() #.splitlines() uses each new line to split the string into a list
print(rawlist)


# In[59]:


total=0
for item in rawlist:
    n=float(item) #convert strings to decimal numbers (i.e. floats)
    total=total+n
print(total)


# Let's write a new file with the total.

# In[60]:


total=str(total) #we need to convert numerics to strings before writing
with open("Day1_TOTAL.txt","w") as txtfile: #like "r" above, "w" specifies that we're writing to the file
    txtfile.write(total)


# <center>
# <h3>Exercises</h3>
# </center>
# 
# * Use a loop to extend the above to get the total for each of the three files, Day1.txt, Day2.txt, and Day3.txt. Create a new file that contains the overall total.  There shouldn't be any sales over 100, so if you find any exclude them!

# # Data Objects: continued
# 
# Last week, we introduced a number of important data structures in Python: string and numeric types, as well as lists.  We used indexing to specify particular parts of the sequential objects - strings and lists.  
# 
# ## Dictionaries
# 
# Dictionaries provide a "mapping object"; instead of an index, they used named "keys" to organized data.  Dictionaries also benefit from faster performance than lists in most cases, due to their use of <a href="https://en.wikipedia.org/wiki/Hash_table">hash tables</a>.  
# 
# A dictionary is defined as follows:

# In[61]:


class_dict = {"course":"Python II","location":"Davis Library","time":"4pm"}
type(class_dict)


# In this case, `"course"`, `"location"`, and `"time"` serve as the "keys" for this dictionary.  Keys play a similar role to the indices we use for lists (or strings).  We can print a particular value by placing its key in the same square brackets `[]` used by list indices.

# In[62]:


print(class_dict["location"])


# A numeric index **will not** work with dictionaries.
# 
# We can also generate a list of all of the keys for a dictionary using the `.keys()` method. 

# In[63]:


print(class_dict.keys())


# ## List and Dictionary Comprehensions
# 
# Python provides some shortcuts to generating lists and dictionaries, especially those that you might (now) generate with a list.  For example, let's generate a list of the square of each number from 1 to 15.

# In[64]:


squares=[]
for n in range(1,16):
    squares.append(n**2)
print(squares)


# Using a "comprehension", we can shorten this to a single line, effectively bringing the loop inside the `[]` used to define the list.

# In[65]:


squares=[x**2 for x in range(1,16)]
print(squares)


# The same general format holds for defining dictionaries.

# In[66]:


squaresdict={k:k**2 for k in range(1,16)}
print(squaresdict)


# We can include conditional statements at the end of the comprehension to build more flexible comprehensions.

# In[67]:


sentence="the quick brown fox jumped over the lazy dog"
sentence=sentence.split(" ") #splits the string into a list with each space
print(sentence)
print([w for w in sentence if len(w)>4])


# <center>
# <h3>Exercises</h3>
# </center>
# 
# * Write a list comprehension to create a list of just the values (i.e. the squares) from `squaresdict`.
# 
# * Write a list comprehension with `os.listdir` to list all of the files in a directory that have a particular extension (e.g. end with .txt).  Try it against a folder in your computer with at least one such file.

# # Defining your own Functions
# 
# While Python (and its available packages) provide a wide variety of functions, sometimes it's useful to create your own.  Python's syntax for defining a function is as follows:
# 
# ```
# def <function_name> ( <arguments> ):
#     <code depending on arguments>
#     return <value>
#         
# ```
# 
# The `mean` function below returns the mean of a list of numbers.  (Base Python does not include a function for the mean.)

# In[68]:


def mean(number_list):
    s=sum(number_list)
    n=len(number_list)
    m=s/n
    return m

numbers=list(range(1,51))
print(mean(numbers))


# <center>
# <h3>Exercises</h3>
# </center>
# 
# Choose one of the following (or both if you're feeling ambitious!):
# * Define a function, `median` to find the median of a list.  The median is the middle number of an odd-numbered list or the average of the middle two numbers in an even numbered list.  (Hint: Use `sorted(<your_list>)` to create a list sorted from low to high values.
# 
# * Define your own function, `variance` to calculate the (population) variance, of a list of numbers:
# 
# $$ \sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i-\mu)^2 $$
# 
# Where $N$ is the length of the list, $x_1, x_2, ... x_N$ are the values in the list, and $\mu$ is the sample average (you can re-use the `mean` function above).  
# 
# 
# * Test your function(s) with the lists below:
# 

# In[69]:


data1 = list(range(1,100))

#Normally Distributed Data:
from numpy.random import normal
data2 = normal(loc=0,scale=2,size=100) #scale=2 defines the standard deviation as 2


# # Try / Except - Making your code robust
# 
# Errors and warnings are a regular occurrence in coding, and an important part of the learning process.  In some cases, they can also be useful in designing an algorithm.  For example, suppose we have a stream of user entered data that is supposed to contain the user's age in years.  You might expect to get a few errors or nonsense entries.

# In[70]:


user_ages=["34","27","54","19","giraffe","15","83","61","43","91","sixteen"]


# It would be useful to convert these values to a numeric type to get the average age of our users, but we want to build something that can set non-numeric values aside.  We can attempt to convert to numeric and give Python instructions for errors with a `try`-`except` statement:

# In[71]:


ages=[]
problems=[]

for age in user_ages:
    try:
        a=int(age)
        ages.append(a)
    except:
        problems.append(age)
        
print(ages)
print(problems)


# # Running Scripts
# 
# We can save our Python code into .py files with File>Save As in Spyder.  A .py file is just a simple text file with a special extension to remind you that it contains Python code.
# 
# We can re-open these files in Spyder with File>Open, and then run or change them.
# 
# ### From the terminal
# We can also run Python scripts directly from the Anaconda Prompt.
# 
# Open your Anaconda Prompt / Anaconda Terminal by:
# * (PC) Start > Anaconda3(64-bit) > Anaconda Prompt
# * (Mac) Finder > Applications > Anaconda Navigator > Environments Tab > (play button listed next to "root") > Open Terminal
# 
# Download [file_explore.py](https://github.com/UNC-Libraries-data/Python/raw/master/Python2/file_explore.py)
# 
# First, we need to point our terminal at the folder containing our .py file.  In the command prompt type: `cd` followed by the path to the folder.
# 
# For example:
# 
#     `cd C:\Users\mtjansen\Desktop\Python\Python2`  
# 
# Then we can execute the script with:
# 
#     `python file_explore.py`
# 
# <center>
# <h3>Exercises</h3>
# </center>
# 
# * What happens when you execute file_explore.py?  Can you think in pseudocode about how the script might work?
# * Use Spyder to open file_explore.py.  Add comments to describe what's happening in each part of the code.  Use a web search or `help()` to get more information about any functions you don't recognize.

# # Useful Packages
# 
# Some of these packages may NOT be included in your Anaconda installation.  Whenever you need to install a package, you need to use the Anaconda prompt window, **NOT Python itself**.  The Anaconda Prompt window can be reached through the Windows Start Menu folder for Anaconda or right clicking and opening a terminal from the Python 3 tab in your Evnironments tab of your Anaconda Navigator on a Mac.
# 
# Installing packages known to Anaconda can be done with the `conda install <package name>` command in your Anaconda Prompt window.  Otherwise you may need to use a different manager like `pip install <package name>`.
# 
# <a href="https://conda.io/docs/user-guide/tasks/manage-pkgs.html">More information about managing packages in Python is available here.</a>

# 
# ## Data Analysis
# 
# ### Numpy and Scipy
# 
# <a href="http://www.numpy.org/">`numpy`</a> provides the mathematical functionality (e.g. large arrayes, linear algebra, random numbers, etc.) for many popular statistical and machine learning tasks in Python.  This is a dependency for many of the packages we discuss below.  <a href="https://docs.scipy.org/doc/scipy/reference/">`scipy`</a> adds an array of mathematical and statistical functions that work with `numpy` objects. 
# 
# ### Pandas 
# 
# The <a href="https://pandas.pydata.org/">`pandas` package</a> provides high-level data manipulation functionality, similar to that found by default in R.  That means new objects like data frames and time series, as well as new functions to manage missing values, merge, and/or reshape datasets.
# 
# Download the csv file <a href="https://github.com/UNC-Libraries-data/Python/raw/master/Python2/CountyHealthData_2014-2015.csv"> 
# CountyHealthData_2014-2015.csv</a>.

# In[72]:


import pandas as pd #pd shortens the name to make it easier to call functions from pandas
os.chdir("C:/Users/mtjansen/Desktop/Python/Python2")

df = pd.read_csv("CountyHealthData_2014-2015.csv")

df.head()


# In[73]:


df.groupby("Region").mean()


# **Learn more:**
# * `pandas` provides a quick introduction <a href="https://pandas.pydata.org/pandas-docs/stable/10min.html">here</a>
# * <a href="https://jakevdp.github.io/PythonDataScienceHandbook/">Python Data Science Handbook</a> provides more detail and integration with other software.
# 
# ### Matplotlib and Visualization
# 
# <a href="https://matplotlib.org/">`matplotlib`</a> is a commonly used data visualization package for Python, oriented towards static, scientific plotting.  There are a number of other packages for visualization including:
# 
# * `seaborn` provides aesthetic extensions to matplotlib
# * `ggplot` - a Python version of the popular ggplot2 package for R
# * `Bokeh` and `Plotly` help create interactive web visualizations
# 
# ## Other Areas
# 
# ### BeautifulSoup (for parsing HTML or XML data)
# 
# Python's built-in `urllib.request` package makes it relatively easy to download the underlying html from a web page. Note that the `from package import function` notation used here allows you to selectively import only parts of a package as needed.

# In[74]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
page = urlopen("https://unc-libraries-data.github.io/Python/Python2/Python-2.html")  #The Python 2 materials!
html = page.read()
print(html[:300]) #print only the first 300 characters


# In[75]:


soup=BeautifulSoup(html,"html.parser")
[x.text for x in soup.find_all("h1")] # find all h1 (top-level headers)


# **Note:** Always check a site's Terms of Service before scraping it.  Some sites explicitly prohibit web scraping of their data.
# 
# ### NLTK (text analysis)
# 
# <a href="http://www.nltk.org/">The Natural Language Toolkit (`nltk`)</a> provides a wide array of tools for processing and analyzing text.  This includes operations like splitting text into sentences or words ("tokenization"), tagging them with their part of speech, classification, and more.
# 
# ## Jupyter Notebooks
# 
# Sooner or later, you'll want to share your code or projects with other people (even if only future-you!).  <a href="http://jupyter.org/">Jupyter notebooks</a>, included with Anaconda, provide integration between code, its output, images, and formatted text beyond what's possible with in-code comments.  The materials for these workshops were created in Jupyter notebooks.
# 
# If you're interested in learning more about Jupyter, consider attending [Jupyter Day in the Triangle](https://libcce.github.io/TriangleJupyter/) at the Carolina Club, Tuesday November 13, 2018.
# 
# ## GitHub
# 
# The materials for this workshop series are maintained in Git and hosted on GitHub.  The materials from our Git / GitHub workshop are available [here](https://github.com/UNC-Libraries-data/Intro-to-Git).
# 
# ## Feedback
# 
# Please fill out our [**Feedback Survey**](http://unc.libsurveys.com/davishubfeedback).
# 
# We'd love your input on future workshop topics and ways we could improve this workshop next time we teach it!

# # Other Resources:
# 
# * <a href="https://jakevdp.github.io/PythonDataScienceHandbook/">Python Data Science Handbook</a>  This free ebook emphasizes Numpy, Scipy, Matplotlib, Pandas and other data analysis packages in Python, assuming some familiarity with the basic principles of the language.
# 
# ### From Python I:
# 
# * <a href="https://automatetheboringstuff.com/">Automate the Boring Stuff with Python</a>
# 
# * <a href="https://stackoverflow.com/questions/tagged/python-3.x?sort=frequent&pageSize=15">Stack Overflow</a>
# 
# * <a href="https://www.google.com/">Google!</a>
# 
# * <a href="http://guides.lib.unc.edu/mattjansen">Make an appointment with Matt</a>
# 
# * <a href="http://www.karsdorp.io/python-course/">Python Programming for the Humanities</a>
# 
# 
