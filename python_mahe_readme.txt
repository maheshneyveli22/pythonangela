https://docs.python.org/3/library/turtle.html

1) Installing packages: 

a) py -m pip install numpy
b) py -m pip install heroes
c) py -m pip install colorgram.py 


2) Libraries installed will be stored in project in the below location:
-> Different projects have different virtual environments 
-> Each one .venv folder 

C:\Workspace\pythonangela\.venv\Lib\site-packages\...

3) Difference between tuple and list 
-> Tuple value cannot be changed while list contents can be changed 
-> Thus tuple is immutable 


4) Pandas:
a) Two primary datastructures of Pandas: series, DataFrame 
-> DataFrame equivalent to whole table. i.e every sheet inside the excel is called a DataFrame 
-> Series: one of the columns of a dataframe or table 

<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.series.Series'>

4) List Comprehension 
-> Creating new list from the previous list 
numbers = [1,2,3]
new_numbers = [new_item for item in list]
--> new_numbers = [n+1 for n in numbers]
name = "Angela"
--> letters_list = [letter for letter in name]

5) conditional list Comprehension
new_list = [new_item for item in list if test]


6) Dictionary Comprehension: Allows to create new Dictionary from the values in a list or dictionary 

new_dict = {new_key: new_value for item in list }

-> Creating new dictionary based on values in existing dictionary 

new_dict = {new_key: new_value for (key,value) in dict.items()}

-> -> Creating new dictionary based on values in existing dictionary  based on condtion

new_dict = {new_key: new_value for (key,value) in dict.items() if test}


7) Handling Exceptions
try: Something that might cause an exception
except: Do this if there was an exception
else: Do this if there were no exceptions
finally: Do this no matter what happens
raise: helps to throw or raise exceptions

8) To run python code in cloud: Use Python Anywhere :
https://www.pythonanywhere.com/


9) HTTP response codes:
1XX - Hold on
2XX - Success, here you go
3XX - go away you dont have permission
4XX - You screwed up
5XX - Server screwed up

10) Python datatypes:
int
str
float
bool

11) sample method specifying return type and arguments with type
##
def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


12) to list environment variables in pycharm : dir env:
PS C:\Workspace\pythonangela> dir env:


13) to access environment variables :
import os
os.environ['no_proxy'] = '*'


14)
-> We can see what can be scraped and what can be :

-> news.ycombinator.com/robots.txt

-> Disallow means that particular endpoint is not allowed for scrapping

15) Python frameworks :

django, flask

16) To run in flask
set FLASK_APP=hello_flask.py


17) How to Generate requirements.txt File in Python?
pip freeze > requirements.txt
-> This command lists all Python packages installed in the current environment and their versions, and redirects the output to a requirements.txt file.

-> to install use:
  pip install -r ./requirements.txt