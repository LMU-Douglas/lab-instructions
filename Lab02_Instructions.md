# Welcome to Lab02! Conditionals and Data Types!

### Data Types

In this lab, you will use the many basic data types avaliable in Python in conjunction with conditionals.

## Notes 
### What are the basic data types?
There are many data types in Python, but we will focus on the basic ones for now. Here are a few:
| Data Type | Description | Example |
| --- | --- | --- |
| `int` | Integer, A whole number that does not have a decimal. | `5` |
| `float` | Floating Point Number, a number that does contain a decimal | `5.0` |
| `str` | String, any text or number in a text-only format | `"Hello, World!"` |
| `bool` | Boolean, a value that represents if something is true or false | `True` or `False` |

We can also cast one type to another. For example, we can cast an integer to a string like this:
```python
x = 5
y = str(x)
```
> In this example, the variable `y` will be a string with the value `"5"`.


### A Brief Overview of Conditionals
Conditionals are used to make decisions in code. They are used to execute a block of code only if a certain condition is true. Here is an example of a conditional in Python:
```python
x = 5
if x > 3:
    print("x is greater than 3")
```
> In this example, the code block `print("x is greater than 3")` will only run if the variable `x` is greater than 3.

We can also use `elif` and `else` statements to add more conditions to our code. Here is an example:
```python
x = 5
if x > 3:
    print("x is greater than 3")
elif x < 3:
    print("x is less than 3")
else:
    print("x is equal to 3")
```

You are also able to have a conditional inside a conditional. This is called a nested conditional. Here is an example:
```python
x = 5
if x > 3:
    print("x is greater than 3")
    if x == 5:
        print("x is equal to 5")
else:
    print("x is less than 3")
```


## Your Lab

|Part | Topic |
| --- | --- |
|A | Personality Quiz|

### Part A ~ **Personality Quiz**

In this scenario, you need to create a personality quiz ala Buzzfeed! ~~#throwbackthursday~~ You will ask the user a series of questions and based on their answers, you will tell them what season they are most like.

First, create a variable to store the user's name. Then, ask the user for their name and store it in the variable.

Next, ask the user a series of questions. You can ask them anything! Each time they answer a question, add a point to the corresponding variable. For example, if they answer "yes" to a question about summer, add a point to the `summer` variable.

Finally, based on their answers, print out a message that tells them what kind of person they are. You can use conditionals to do this.

Each question will use a conditional in some way, shape, or form. Different questions will require different conditionals (i.e. if, elif, else) or may even require nested conditionals. Follow the template below to get started and keep an eye on those types! There may already be something amiss...


```python
# Part A - Intro
# Ask the user for their name and save it to a variable!


# Store their answer in the varibles below.
summer = 0
fall = 0
winter = 0
spring = 0

# Part B - Questions

# Question #1
print("What color do you like the most?")
print(" 1) Red")
print(" 2) Blue")
print(" 3) Green")
print(" 4) Yellow")
color = input("Enter the number of your choice: ")

if color == 1:
    summer += 1

# TODO: Finish the if statement above

# Question #2
# Do you like warm or cold?
# If they like warm, add a point to summer and spring
# If they like cold, add a point to fall and winter

# Question #3
# Do you like drinking warm drinks or cold drinks?
# If they like hot chocolate, ask them if the like hot cocoa or tea
# If they like hot cocoa, add a point to winter
# If they like tea, add a point to spring
# If they like cold drinks, ask them if they like lemonade or iced tea
# If they like lemonade, add a point to summer
# If they like iced tea, add a point to fall

# Question #4
# What activity do you like to do outside?
# If they like to swim, add a point to summer
# If they like to ski, add a point to winter
# If they like to garden, add a point to spring
# If they like to hike, add a point to fall

# Question #5
# What month were you born in?
month = input("What month were you born in? ")
# If they were born in June, July, or August, add a point to summer
# If they were born in September, October, or November, add a point to fall
# If they were born in December, January, or February, add a point to winter
# If they were born in March, April, or May, add a point to spring

# Part C - Results

# Based on the answers, print out the season they are most like!
# Use conditionals to do this.

# How can you find the House with the max count?
# Remember that in the event of a tie, the user should be sorted into
# the season in alphabetical order, so if there is a tie between summer 
# and spring, the user should be sorted into spring.

season = 'None'

max_score = 0

if summer > max_score:
    season = 'Summer'
    max_score = summer

#TODO: Finish the if statement above for the rest of the seasons


#The following code does not need to be changed

print("Thank you for taking the quiz", name, "!")
print("You are most like", season)
```



