# user-defined functions
# i.regular functions:these will have static behaviour
def sample():
    print("hello world")
sample()
# ii.parameterized functions: these will take one or more parameters
# 1.default parameters: these parameters will have default values
def add(x,y=5):
    print("x :",x)
    print("y :",y)
add(10)
# 2.keyword parameters: these parameters will be passed by Keyboard
def person(name,age):
    print("name:",name)
    print("age:",age)
person(age=25,name="john")
# 3. positional parameters: these parameters will be passed by position
def add(a,b):
    print("a:",a)
    print("b:",b)
add(10,20)
# 4. arbitary parameters: these parameters will take multiple values
def sample(*x):
    print(x)
sample(10,20,30,40)
# iii.return functions: these functions will return a value
def add(x,y):
    return x+y
result=add(10,20)
# iv. void functions: these functions will not return any value
def sample():
    print("hello world")
sample()
# v. lambda functions: these are anonymous functions
add=lambda x,y:x+y
result=add(10,20)
print("result:",result)